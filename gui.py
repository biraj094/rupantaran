import streamlit as st
import rupantaran.land.hilly as hilly
import rupantaran.land.terai as terai
import rupantaran.land.cross_system as cross_system
import rupantaran.land.mixed_units as mixed_units

def main():
    st.title("Land Measurement Converter")
    
    st.info("""
    **Supported Units:**
    - **Hilly System:** Ropani, Aana, Paisa, Daam
    - **Terai System:** Bigha, Kattha, Dhur
    - **Conversions Available:**
      - Convert between Hilly and SI units
      - Convert between Terai and SI units
      - Convert between Hilly and Terai units
      - Convert mixed expressions (e.g., '1 ropani 2 aana')
    
    **Examples:**
    - Convert 2 ropani to square meters
    - Convert 5 bigha to kattha
    - Convert '1 bigha 5 kattha' to SI units
    """)
    
    conversion_type = st.selectbox("Select Conversion Type", [
        "Hilly to SI",
        "Terai to SI",
        "Cross System Conversion",
        "Mixed Unit Conversion"
    ])
    
    if conversion_type == "Hilly to SI":
        st.subheader("Convert Hilly Land Units to SI")
        value = st.number_input("Enter Value", min_value=0.0, format="%.2f")
        from_unit = st.selectbox("From Unit", ["ropani", "aana", "paisa", "daam"])
        if st.button("Convert"):
            result = hilly.hilly_to_sq_meters(value, from_unit)
            st.success(f"Equivalent in SI Units: {result} square meters")
    
    elif conversion_type == "Terai to SI":
        st.subheader("Convert Terai Land Units to SI")
        value = st.number_input("Enter Value", min_value=0.0, format="%.2f")
        from_unit = st.selectbox("From Unit", ["bigha", "kattha", "dhur"])
        if st.button("Convert"):
            result = terai.terai_to_sq_meters(value, from_unit)
            st.success(f"Equivalent in SI Units: {result} square meters")
    
    elif conversion_type == "Cross System Conversion":
        st.subheader("Convert Between Hilly and Terai Systems")
        unit_type = st.selectbox("Convert From", ["Hilly to Terai", "Terai to Hilly"])
        value = st.number_input("Enter Value", min_value=0.0, format="%.2f")
        if unit_type == "Hilly to Terai":
            from_unit = st.selectbox("From Unit", ["ropani", "aana", "paisa", "daam"])
            to_unit = st.selectbox("To Unit", ["bigha", "kattha", "dhur"])
            if st.button("Convert"):
                result = cross_system.hilly_to_terai(value, from_unit, to_unit)
                st.success(f"Equivalent in Terai Units: {result}")
        else:
            from_unit = st.selectbox("From Unit", ["bigha", "kattha", "dhur"])
            to_unit = st.selectbox("To Unit", ["ropani", "aana", "paisa", "daam"])
            if st.button("Convert"):
                result = cross_system.terai_to_hilly(value, from_unit, to_unit)
                st.success(f"Equivalent in Hilly Units: {result}")
    
    elif conversion_type == "Mixed Unit Conversion":
        st.subheader("Convert Mixed Units")
        expression = st.text_input("Enter Mixed Unit Expression (e.g. '1 ropani 2 aana')")
        conversion_type = st.selectbox("Convert To", ["SI Units", "Hilly Mixed", "Terai Mixed"])
        if st.button("Convert"):
            if conversion_type == "SI Units":
                if any(unit in expression for unit in ["bigha", "kattha", "dhur"]):
                    result = mixed_units.parse_terai_mixed_unit(expression)
                else:
                    result = mixed_units.parse_hilly_mixed_unit(expression)
                st.success(f"Equivalent in SI Units: {result} square meters")
            elif conversion_type == "Hilly Mixed":
                result = mixed_units.terai_mixed_to_hilly_mixed(expression)
                st.success(f"Equivalent in Hilly Units: {result}")
            else:
                result = mixed_units.hilly_mixed_to_terai_mixed(expression)
                st.success(f"Equivalent in Terai Units: {result}")
    
if __name__ == "__main__":
    main()