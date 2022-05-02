import turtle

turtle.bgcolor("black")
turtle = turtle.Turtle()
turtle.shape("turtle")
turtle.speed(3)
turtle.width(10)
turtle.color("blue", "yellow")
turtle.pencolor("red")
turtle.penup()

while True:
    command: list[str] = input("🐢>").strip().split()
    match command:
        case ["move", *points]:
            match points:
                case [x, y]:
                    turtle.goto(float(x), float(y))
                case [steps]:
                    turtle.forward(float(steps))
        case ["turn", *options]:
            match options:
                case [angle]:
                    turtle.right(float(angle))
                case _:
                    turtle.right(90)
        case ["draw", shape, size]:
            turtle.pencolor("red")
            turtle.pendown()
            match shape:
                case "circle":
                    turtle.circle(float(size))
                case "line":
                    turtle.forward(float(size))
            turtle.penup()
        case ["write", *text]:
            turtle.write(" ".join(text), None, "center", "16pt 20")
        case ["exit" | "stop" | "quit"]:
            break
        case _:
            print("Invalid command")
    
#     command = input("Aonde?").strip()
#     if command == "line":
#         turtle.pendown()
#         turtle.forward(90)
#         turtle.penup()
#     elif command == "circle":
#         turtle.pendown()
#         turtle.circle(100)
#         turtle.penup()
#     elif command == "exit":
#         break
        
        
#     turtle.goto(*position)
#     turtle.pendown()
#     turtle.forward(90)
#     turtle.penup()
#     turtle.right(90)
#     turtle.forward(20)
    
#     position[0] += 5
#     position[1] += 5
