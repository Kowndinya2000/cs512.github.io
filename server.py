from flask import Flask, request
from flask import Blueprint, render_template, redirect, url_for, request, flash
app = Flask(__name__, template_folder='template')
import os
# import collections

@app.route('/', methods=['GET'])
def home():
    print(os.getcwd())
    ''' Renders the home page (start screen)
    '''
    return render_template('home.html')

@app.route('/home', methods=['GET'])
def home2():
    ''' Renders the home page (start screen)
    '''
    return render_template('index.html')

@app.route('/build/<graph_id>', methods=['GET'])
def percolate_the_graph(graph_id):
    graph = "g"+str(int(graph_id)+1)+".html"
    return render_template(graph)
 
#Starting function to start the connection on the port 5002 and running on 
# the ip 0.0.0.0 

if __name__ == '__main__':
	app.run(debug=True)