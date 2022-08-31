![LFIscanner](https://user-images.githubusercontent.com/75953873/177439268-5a14bd8b-c2ce-4ba1-98a8-e014bd9e0829.png)

<h1 align="center"></h1>

Local File Inclusion (LFI) scanner.

## Usage
| COMMAND | DESCRIPTION |
| ------------- | ------------- |
| -t / --target | Target |
| -p / --payload | Payload file |
| -e / --extract | Extract content |
| -h / --help | Request help |

## Instalación / Installation
```
> git clone https://github.com/R3LI4NT/LFIscanner

> cd LFIscanner

> pip3 install -r requirements.txt
```

</br>

</br>


`EXAMPLE:` **Detectar payloads LFI**
```python
python3 LFIscanner.py -t http://192.168.25.131/mutillidae/?page= -p <payload-file>
```

![example](https://user-images.githubusercontent.com/75953873/177440070-5526fe9c-8455-492e-b0f6-eb47dfef74d6.png)

`EXAMPLE:` **Extraer información del payload LFI**
```python
python3 LFIscanner.py -t http://192.168.25.131/mutillidae/?page= --payload <payload-file> --extract
```

![example_2](https://user-images.githubusercontent.com/75953873/177440180-2e4eebbd-1b5b-44af-8d09-0b1e9ba4175e.png)

</br>

Payloads file by: https://github.com/emadshanab/LFI-Payload-List
