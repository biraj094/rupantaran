
# Rupantaran

<!-- [![PyPI](https://img.shields.io/pypi/v/rupantaran)](https://pypi.org/project/rupantaran/)  
[![TestPyPI](https://img.shields.io/badge/TestPyPI-Testing-blue)](https://test.pypi.org/project/rupantaran/)   -->
<!-- [![License](https://img.shields.io/github/license/yourusername/rupantaran)](LICENSE) -->

**Rupantaran** is a Python package that converts various **Nepali-specific measurements** into **SI units** or commonly used metric units.  

---

## 📌 Supported Measurement Categories

This package covers a range of traditional Nepalese measurement units, including:

- [X] **Land**: <del>khetmuri</del>, bigha, kattha, dhur, ropani, aana, paisa, dam  
- [ ] **Volume**: mutthi, mana, pathi, dabba  
- [ ] **Length**: angul, dharnugrah, dhanurmushti, vitastaa, haath, kosh, yojan  
- [ ] **Weight**: dharni, Taul  
- [ ] **Valuable Metals**: lari, tola, pahadi  

The package ensures accurate conversions by cross-referencing multiple resources.  

---

## 📚 Conversion References

1. [Wikipedia - Nepalese Units of Measurement](https://en.wikipedia.org/wiki/Nepalese_units_of_measurement)
2. [Mero Kalam - Land Measurement](https://www.merokalam.com/nepali-land-measurement/)
3. [Ministry of Land Reform Conversion Tool](https://www.dos.gov.np/tools/unit)
4. [Rotaract - Unit Conversion PDF](https://www.nepalhelp.dk/filer/Projecthelp/conversion.pdf)
5. [1990 JICA Conversion Table](https://openjicareport.jica.go.jp/pdf/10812329_01.pdf)

---

## Environment Setup Guide for Rupantaran

This document provides a step-by-step guide to setting up the development, staging, and production environments for the **rupantaran** package.


### 📌 1. Development Environment (dev)

This environment is used **only for local testing**. **Do not upload anything from dev to PyPI.**

#### ✅ Steps to Set Up the Development Environment:

1. **Activate the development environment:**
   ```sh
   conda activate env-rupantaran-dev
   ```

2. **Install the package in editable mode:**
   ```sh
   pip install -e .
   ```
   - This allows you to make changes to the package and test them without reinstalling it.

3. **Run tests to verify installation:**
   ```sh
   pytest
   ```

---

### 📌 2. Staging Environment (stage) → TestPyPI

This environment is used for **publishing the package to TestPyPI**, PyPI's testing server.

#### ✅ Steps to Set Up the Staging Environment:

1. **Activate the staging environment:**
   ```sh
   conda activate env-rupantaran-stage
   ```

2. **Install required dependencies for building and uploading the package:**
   ```sh
   pip install build twine
   ```

3. **Build the package:**
   ```sh
   python -m build
   ```
   - This generates the `dist/` directory containing `.tar.gz` and `.whl` files.

4. **Upload the package to TestPyPI:**
   ```sh
   twine upload --repository testpypi dist/*
   ```
   - You will need an **API Key** for authentication.

5. **Install the package from TestPyPI to verify deployment:**
   ```sh
   pip install --index-url https://test.pypi.org/simple/ rupantaran
   ```

6. **Run tests on the installed package:**
   ```sh
   pytest --pyargs rupantaran
   ```

---

### 📌 3. Production Environment (prod) → Final PyPI Upload

This environment is used for **publishing the final package to PyPI**.

#### ✅ Steps to Set Up the Production Environment:

1. **Activate the production environment:**
   ```sh
   conda activate env-rupantaran-prod
   ```

2. **Upload the final version to PyPI:**
   ```sh
   twine upload dist/*
   ```
   - This makes the package available on the **official PyPI repository**.

---

## Documentation 

1. Navigate to directory
    ```
    cd rupantaran/docs
    ```
2. Generate the docs
    ```
    make html
    ```
3. Serve the docs in localhost
    ```
    sphinx-autobuild . _build 
    ```

---

## 🛠 Additional Notes

- Always **test the package in the staging environment** before publishing to production.
- If needed, remove the `dist/` directory before rebuilding the package:
  ```sh
  rm -rf dist/
  ```
- If you face authentication issues, regenerate the **API token** from TestPyPI or PyPI and update your `~/.pypirc` file.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.











