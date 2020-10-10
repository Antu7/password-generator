# Password Generating Tools Using Python
Command line tool to generate passwords for brute forcing.
For Brute Force attack please check this Medium blogpost [here](https://medium.com/@textmeantu/brute-force-attack-with-python-c1d70fcba607)



## Installation
 Clone the repo
```bash
git clone https://github.com/Antu7/password-generator.git
```
or you can use Github CLI <font color='green'>(new)</font>
```bash
gh repo clone Antu7/password-generator
```


### Optional
You can add this line to ```~/.bashrc``` to enable this program globaly.
```bash
alias passgen="~/password-generator/passswordGenerator.py"
```



## Run
```bash
cd password-generator
python passwordGenerator.py [-flags]
```

### Or
Use this if you have added an alias to ```~/.bashrc```
```bash
passgen [-flags]
```


## Usage
```bash
python passwordGenerator.py -p POSSIBLECOMBO -c COMBINATIONTYPE
```
#### Arguments
|args|description|parameters||
|----|-----------|-|-|
|-h|show help meesage|||
|-p|Number of characters in password||default = 3|
|-c|Possible options for password combination type|1,2,3,4,5|REQUIRED|



Possible options for password combination type:

1.  Combination Alphnumeric .
2.  Combination Character only .
3.  Combination Special Character Only .
4.  Combination Special Character and number only .
5.  Combination Alphanumeric Special Character .




## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
