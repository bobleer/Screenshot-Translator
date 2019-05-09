# Screenshot-Translator

An Alfred workflow for translating screenshot by employing [Translate Tab.app](http://translate-tab.com/) and [Tesseract-ocr](https://github.com/tesseract-ocr/tesseract)

## Preview

![](https://github.com/bobleer/Screenshot-Translator/raw/master/preview/1.gif)

![](https://github.com/bobleer/Screenshot-Translator/raw/master/preview/2.gif)

![](https://github.com/bobleer/Screenshot-Translator/raw/master/preview/3-1.gif)

## Requirements

0. macOS...
1. [Alfred3.app](https://www.alfredapp.com/)
2. [Translate Tab.app](http://translate-tab.com/)
3. [Tesseract-ocr (Open Source)](https://github.com/tesseract-ocr/tesseract)
4. [Plain Clip (Open Source)](https://www.bluem.net/en/projects/plain-clip/)

```console
brew install tesseract
```

## Install Workflow

1. [Download this workflow](https://github.com/bobleer/Screenshot-Translator/raw/master/QuickTranslate.alfredworkflow)
2. Click and import it to Alfred Workflow, and set a hothey you want
3. Download [textclean.py](https://raw.githubusercontent.com/bobleer/Screenshot-Translator/master/textclean.py)
3. Modify Translate Tab setting to 'Automatically translate clipboard'
Finished!

**Then using hotkey to launch screenshot and translator.**

NOTE:
1. The screenshots will not be saved by default.
2. Using workflow will cover clipboard content. 
3. Translate Tab is hard to use in China.
