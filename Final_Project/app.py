from password import app

def custom1(input):
    List1=[]
    for i in input:
        List1.append(i)
    return List1
if __name__ == '__main__':
    app.run(debug=True)
