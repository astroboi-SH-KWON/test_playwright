# test_playwright
https://playwright.dev/python/docs/intro


# Setting up the Environment  
    1. Set conda env
        if silicon mac:
            conda create -n playwright python==3.12.3
            conda activate playwright

            conda config --add channels conda-forge
            conda config --add channels microsoft
            conda install playwright==1.44.0
            playwright install  # # Install the required browsers like chromium, Firefox, Webkit, FFMPEG
            
            conda install anaconda::beautifulsoup4==4.12.2

