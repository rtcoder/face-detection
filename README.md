# face detection

## INSTALATION
`pip install -r requirements.txt`

## USAGE
`python main.py <file> [options]`

### Options

| OPTION | DEFAULT | DESCRIPTION |
| ------------- |:-------------:| -----:|
|`-h or --help`| - |display help|
|`-c or --cli`| 1 |Values 1 or 0. Turns on/off CLI mode. 1 shows only face locations, 0 displays window with rectangle on detected faces|
|`-r or --rotate`| 1 |Values 1 or 0. if 1 then image is rotated to find face when at first time no face is detected|

### RETURNS

returns list of faces coordinates in format below

`[(top, right, bottom, left)]`
