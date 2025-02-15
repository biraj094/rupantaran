# Rupantaran

[![PyPI](https://img.shields.io/pypi/v/rupantaran)](https://pypi.org/project/rupantaran/)  
[![TestPyPI](https://img.shields.io/badge/TestPyPI-Testing-blue)](https://test.pypi.org/project/rupantaran/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![codecov](https://codecov.io/gh/biraj094/rupantaran/graph/badge.svg?token=FQRYN84524)](https://codecov.io/gh/biraj094/rupantaran)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/biraj094/rupantaran/badge)](https://scorecard.dev/viewer/?uri=github.com/biraj094/rupantaran)
[![Deployment-PyPiProd](https://github.com/biraj094/rupantaran/actions/workflows/Deployment-PyPiProd.yml/badge.svg)](https://github.com/biraj094/rupantaran/actions/workflows/Deployment-PyPiProd.yml)
[![Deployment-testPyPi](https://github.com/biraj094/rupantaran/actions/workflows/Deployment-testPyPi.yml/badge.svg)](https://github.com/biraj094/rupantaran/actions/workflows/Deployment-testPyPi.yml)
[![Deploy-docs](https://github.com/biraj094/rupantaran/actions/workflows/deploy-docs.yml/badge.svg)](https://github.com/biraj094/rupantaran/actions/workflows/deploy-docs.yml)

---

<p align="center">
  <img src="rupantaran.png" alt="Rupantaran Logo" width="200" height="200">
</p>

**Rupantaran** is a Python package that converts various **Nepali-specific measurements** into **SI units** or commonly used metric units.  You can read the docs [here](https://rupantaran.readthedocs.io/en/latest/).

---

## 📌 Supported Measurement Categories

This package covers a range of traditional Nepalese measurement units, including:

- [X] **Land**: <del>khetmuri</del>, bigha, kattha, dhur, ropani, aana, paisa, dam , square meter  
- [ ] **Volume**: mutthi, mana, pathi, dabba  
- [ ] **Length**: angul, dharnugrah, dhanurmushti, vitastaa, haath, kosh, yojan  
- [X] **Weight**: lal, tola, chatak, pau, dharni, sher, kg, g, lb, oz  

The package ensures accurate conversions by cross-referencing multiple resources. Please create an issue if you find any discrepancies in conversion maps. [This](https://docs.google.com/spreadsheets/d/1Y_XrdH4gqVXVI-ek8ZDeLZxoGFjHQYAhC8UeeU8hT5w/edit?usp=sharing) sheet contains the conversion maps for the weight unit. Also, please let create an issue if you find any updated conversion maps.

---

## 📚 Conversion References

1. [Wikipedia - Nepalese Units of Measurement](https://en.wikipedia.org/wiki/Nepalese_units_of_measurement)
2. [Mero Kalam - Land Measurement](https://www.merokalam.com/nepali-land-measurement/)
3. [Ministry of Land Reform Conversion Tool](https://www.dos.gov.np/tools/unit)
4. [Rotaract - Unit Conversion PDF](https://www.nepalhelp.dk/filer/Projecthelp/conversion.pdf)
5. [1990 JICA Conversion Table](https://openjicareport.jica.go.jp/pdf/10812329_01.pdf)

---

## Environment Setup Guide for Rupantaran

**This document provides a step-by-step guide to setting up the development and production environments for the **rupantaran** package.**

### 📌 Development Environment 

This environment is used for publishing the package to TestPyPI, PyPI's testing server. This is facilated with [GitHub Actions workflow](.github/workflows/Deployment-testPyPi.yml). The TestPyPI link for rupantaran is [here](https://test.pypi.org/project/rupantaran/).


<details>
  <summary>
  Expand for more details for the development environment
  </summary> 

---

<blockquote>
   <b>Note:</b> The GitHub Actions workflow is configured to run automatically when a new tag is pushed to the repository. This ensures that the package is always built and uploaded to TestPyPI when a new version is released.
</blockquote>

<br>

```python
# Always create a tag after the version_id is updated in the setup.py file.
# Create a new tag
git tag v0.2.2
# Push the tag to the repository
git push origin v0.2.2
```

<br>

#### ✅ Steps to Set Up the Development Environment:

1. **Activate the development environment:**
   ```sh
   conda activate env-rupantaran-dev
   ```

2. **Install required dependencies for building and uploading the package:**
   ```sh
   pip install build twine
   ```

3. **Build the package and install it in editable mode:**
   ```sh
   python -m build
   pip install -e .
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
</details>

### 📌 Production Environment  

This environment is used for publishing the final package to PyPI.This is facilated with [GitHub Actions workflow](.github/workflows/Deployment-PyPiProd.yml). The PyPI link for rupantaran is [here](https://pypi.org/project/rupantaran/).

<details>
  <summary>
  Expand for more details for the production environment
  </summary>

---

<blockquote>
   <b>Note:</b> The Github Action workflow is configured to push the package to PyPI when a PR is merged into the main branch. 
</blockquote>


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
</details>

---

## Documentation 

The documentation is built with [Sphinx](https://www.sphinx-doc.org/en/master/) and [Read the Docs](https://readthedocs.org/). The documentation is stored in the `docs/` directory. This is facilitated with [GitHub Actions workflow](.github/workflows/deploy-docs.yml). This workflow checks if there are any changes in the `docs/` directory and if so, it builds the documentation .

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

## Testing

Some useful commands for testing the package:

```
# Check the coverage of the all files
pytest --cov=rupantaran  --cov-report=term-missing 
# Run the tests for a specific keyword
pytest -k "hill"  
# Generate the coverage report in html format
pytest --cov=rupantaran  --cov-report=html   

```

   


## 🛠 Additional Notes

- Always **test the package in the staging environment** before publishing to production.
- If needed, remove the `dist/` directory before rebuilding the package:
  ```sh
  rm -rf dist/
  ```
- If you face authentication issues, regenerate the **API token** from TestPyPI or PyPI and update your `~/.pypirc` file. This is not relevant here, because we are using GitHub Actions to upload the package to TestPyPI and PyPI.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
 









