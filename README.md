Certificate Batch Generator
This repository contains the Certificate Batch Generator, a Python-based tool developed using Streamlit to automate the process of generating certificates for participants in events such as hackathons. The application allows users to quickly generate certificates from a template and an Excel file containing participant names, with various customization options.

Features
Excel and PDF Upload: Users can upload an Excel file containing participant names and a PDF file to serve as the certificate template.
Customizable Name Placement: Adjust the vertical and horizontal placement of the name on the certificate using offset sliders.
Font Customization: Choose the font color and adjust the font size. The font size automatically adjusts based on the length of the name.
Preview Feature: Generate a preview of a single certificate to verify name placement before mass generation.
Batch Generation: Once satisfied with the preview, generate all certificates with a single click.
Downloadable Output: The generated certificates are zipped and provided for download.
Installation
To get started with the Certificate Batch Generator, follow these steps:

Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/certificate-batch-generator.git
Navigate to the project directory:

bash
Copy code
cd certificate-batch-generator
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Streamlit application:

bash
Copy code
streamlit run app.py
How to Use
Upload the Excel file containing the list of participant names.
Upload the PDF file that will serve as the certificate template.
Select the appropriate column from the Excel file that contains the names.
Use the sliders to adjust the name’s position on the certificate.
Customize the font color and size, and generate a single preview certificate to verify the placement.
Once satisfied with the placement, click to generate the batch of certificates.
Download the zipped folder containing all the certificates.
Challenges
Due to Streamlit's limitations with real-time JavaScript integrations, the application does not support real-time previews. To address this, a feature was introduced that allows users to generate a single preview certificate for adjustments before generating the entire batch.

Future Scope
The application has proven efficient and could be commercialized for use by other organizations in automating certificate generation for events and hackathons.

Contributing
Contributions are welcome! Please fork this repository and submit a pull request if you'd like to contribute improvements or features.
