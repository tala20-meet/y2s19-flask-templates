from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
	opposite_day=True
	favorite_food=["sushi","dawali","spaghetti"]
	least_favorite_food=["tkg"]
	return render_template("index.html",list1=favorite_food,opposite_day=opposite_day,least_favorite_food=least_favorite_food)



if __name__ == '__main__':
   app.run(debug = True)
