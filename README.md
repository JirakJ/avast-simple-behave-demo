# avast-simple-behave-demo
To run this project you will need update location of Google Chrome web driver

#Steps to run this project:
    
    git clone https://github.com/JirakJ/avast-simple-behave-demo.git
    cd avast-simple-behave-demo
    
Than update path to Google Chrome webdriver in:
    
    features/steps/avastBuyUltimateVersion.py on line 9
    
And after that continue with: 

    python3 -m virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    behave

#Tested with:
    
    Google Chrome: Verze 91.0.4472.114 (Oficiální sestavení) (arm64)
    Chrome web driver: 91.0.4472.101 available from: https://chromedriver.storage.googleapis.com/91.0.4472.101/chromedriver_mac64_m1.zip