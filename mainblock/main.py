from mainblock import app
from flask import render_template, jsonify, request
from mainblock.controlgpio import true_dict, check_status, pk1, pk2, pk3, pk4


@app.route('/')
def url():
    return render_template('index.html')


@app.route('/checkall', methods=['GET', 'POST'])
def check():
    check_status()
    return true_dict


@app.route('/turniping', methods=['GET', 'POST'])
def pin_on():
    flag = request.args.get('flag')
    mode = request.args.get('mode')

    if flag == "pk1":
        pk1(mode)
    if flag == "pk2":
        pk2(mode)
    if flag == "pk3":
        pk3(mode)
    if flag == "pk4":
        pk4(mode)

    return "Zrobione!"
