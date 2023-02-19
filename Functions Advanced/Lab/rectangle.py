def rectangle(l,w):
    if type(l) != int or type(w) != int:
        return 'Enter valid values!'
    def area():
        return l*w
    def perimeter():
        return 2*(l+w)
    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"

print(rectangle(2, 10))