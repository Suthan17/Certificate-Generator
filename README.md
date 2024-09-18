# Certificate Batch Generator

This repository contains the **Certificate Batch Generator**, a Python-based tool developed using **Streamlit** to automate the process of generating certificates for participants in events such as hackathons. The application allows users to quickly generate certificates from a template and an Excel file containing participant names, with various customization options.

## Features

- **Excel and PDF Upload**: Users can upload an Excel file containing participant names and a PDF file to serve as the certificate template.
- **Customizable Name Placement**: Adjust the vertical and horizontal placement of the name on the certificate using offset sliders.
- **Font Customization**: Choose the font color and adjust the font size. The font size automatically adjusts based on the length of the name.
- **Preview Feature**: Generate a preview of a single certificate to verify name placement before mass generation.
- **Batch Generation**: Once satisfied with the preview, generate all certificates with a single click.
- **Downloadable Output**: The generated certificates are zipped and provided for download.

## Installation

To get started with the **Certificate Batch Generator**, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/certificate-batch-generator.git
