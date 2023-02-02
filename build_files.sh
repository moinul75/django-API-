

echo " BUILD START"
python3 -m pip install -r requirements.txt 
python3 manage.py collections --noinput --clear
echo " BUILD END"
