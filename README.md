# rupantaran

This project aims to create a Python package to convert various Nepali specific measurements to SI or commonly used units. 



# Measurement metrics categories:

1. Land (khetmuri/bigha/kattha/dhur/ropani/aana/paisa/dam)
2. Volume (mutthi/mana/pathi/dabba)
3. Length  (angul/dharnugrah/dhanurmushti/vitastaa/haath/kosh/yojan)
4. Weigth (dharni/Taul)
5. Valuable Metals (lari/tola/pahadi)


# Resources for conversion

1. [Wikipedia](https://en.wikipedia.org/wiki/Nepalese_units_of_measurement)
2. [Blog](https://www.merokalam.com/nepali-land-measurement/)
3. [Ministry of Land Reform](https://www.dos.gov.np/tools/unit)
4. [PDF from Rotaract](https://www.nepalhelp.dk/filer/Projecthelp/conversion.pdf)
5. [1990 conversion table from JICA](https://openjicareport.jica.go.jp/pdf/10812329_01.pdf)

Cross reference each unit to see which one is most likely to be used.



TOOLS 
- pytest
- sphinx
- pip install sphinx-autobuild sphinx-rtd-theme





# ENV Setup

```python
    conda activate env-rupantaran-dev
    # For pytest to easily find your package, install rupantaran in editable mode. In the root of your project (the parent directory of rupantaran/), run:
    pip install -e .
    pytest
```


# To run the docs

1. Navigate to <code>rupantaran/docs</code>
2. Run <code>make html</code> to generate new docs files.
3. Run <code>sphinx-autobuild . _build </code> to serve the docs in localhost.



# FOR TEST 

1. From root directory <code>pytest</code>