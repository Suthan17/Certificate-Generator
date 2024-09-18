
# Certificate Batch Generator

This project is a Streamlit-based application for automating the generation of certificates in batch. It allows users to upload an Excel file containing participant names and a PDF certificate template. The app automatically places the participant names on the certificate, allowing for customization of font size, color, and name placement.

## Features

- Upload an Excel file with participant names and a PDF certificate template.
- Customize the vertical and horizontal placement of names on the certificate.
- Adjust font size and color for the participant names.
- Preview a single certificate before generating the entire batch.
- Generate and download certificates for all participants with a single click.
- Auto-adjusts font size based on the name length to fit neatly on the certificate.

## App Functionality

1. Upload an Excel spreadsheet containing the list of names and a PDF serving as the certificate template.
2. Select the desired column from the Excel file to extract names.
3. Use the sliders to adjust vertical and horizontal offsets for name placement.
4. Customize the font color and size as needed.
5. Preview a single certificate to verify placement and adjustments.
6. Generate all certificates in a batch after making necessary adjustments.
7. Download the certificates in a zip file.

## Prerequisites

Ensure that you have Python 3.7+ installed on your system.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/certificate-batch-generator.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd certificate-batch-generator
   ```

3. **Create and activate a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. **Install the required dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Streamlit app**:

   ```bash
   streamlit run app.py
   ```

2. **Upload the required files**:
   - Excel file with the list of participant names.
   - PDF template for the certificate.

3. **Customize the certificate**:
   - Choose the column for names from the Excel sheet.
   - Adjust the vertical and horizontal offsets for name placement.
   - Customize font size and color.

4. **Preview and generate certificates**:
   - Preview a single certificate to adjust the settings.
   - Generate certificates for all participants in a batch.
   - Download the zipped file containing all generated certificates.

## Challenges

- **Real-time Preview**: The app does not support real-time preview due to Streamlit’s limited JavaScript support. As a solution, a single certificate preview is available before batch generation.

## Future Scope

- The company plans to commercialize the application to offer it as a service for organizing hackathons and similar events.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
