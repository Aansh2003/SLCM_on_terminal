# SLCM terminal scraper

This project has been made by my sheer hatred for the Student Life Cycle Management website(SLCM) for my university. [SLCM](https://slcm.manipal.edu/)\

If you're tired of having to open this website to view basic details like attendance and internal marks, set up this package and get various functionalities through the command line directly.\

## Linux setup

Clone the repository

Install Tesseract OCR module
```
sudo apt install tesseract-ocr -y
```

Install python dependencies
```
pip3 install -r requirements.txt
```

Make setup shell script executable
```
chmod +x setup.sh
./setup.sh
```

Update the parameters in **parameters.py**\
Setup is done, use the following commands to view slcm attendance and internal marks.

```
slcm-attendance
slcm-internals
```