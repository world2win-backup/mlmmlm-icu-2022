# url
https://revorevo.gitlab.io/mlmmlm-icu-2022

https://o.mlm01.icu 
(will expire in one year)

# wget
` wget --wait=0.3 -r -l 2 -p -E -k -np -K -e robots=off -i urls.txt`
use `-l 2` instead of `-l 1` to backup uploads.

## whole site backup

by default `-r` is eq to `-r -l 5`

you may use 
```
wget --wait=0.2 -K -e robots=off --mirror --convert-links --adjust-extension --page-requisites --no-parent https://site-to-download.com
```
to backup entire site

# urls.txt
```
https://mlmmlm.icu/latest?no_definitions=true
https://mlmmlm.icu/latest?no_definitions=true&page=1
https://mlmmlm.icu/latest?no_definitions=true&page=2

```
# ipfs

`ipfs resolve -r QmZMAFngPr2XkWZ1bMpSKv6frAw2df7ZsPS5bdwDf8JYxy`


`ipfs get QmZMAFngPr2XkWZ1bMpSKv6frAw2df7ZsPS5bdwDf8JYxy`


or

https://ipfs-gateway.cloud/ipfs/QmZMAFngPr2XkWZ1bMpSKv6frAw2df7ZsPS5bdwDf8JYxy

https://bafybeifdsh3npdqynjbtmoiynhgdtpqava4qt7kafhrppnyx2mqvqjvd4i.ipfs.dweb.link/

for commit/980571c2d422389e5cc52780bc1d67fd778f47a7

## see also

https://ipfs.github.io/public-gateway-checker/

https://github.com/ipfs/notes/issues/424

https://github.com/ipfs/kubo/issues/3908
