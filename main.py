from flask import Flask, request, redirect

app = Flask(__name__)
div = {}

@app.route('/')
def a():
    return """<!DOCTYPE html>
            <html lang="en">
            
            <head>
                <link rel="stylesheet" href="/static/style.css">
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>HotelSerch</title>
            </head>
            <body>
                <div>
                    <header class="header">
                        <div class="logo-home">     
                            <img src="/static/imgrs/Group 3311.png" alt="">
                            <p style="padding-top: 16px;">Building</p>
                        </div>
                        <div style="padding-top: 18px;">
                            <ul class="header-list">
                                <li> <a href="#Home">Home</a></li>
                                <li> <a href="#Service">Services</a></li>
                                <li> <a href="#About">About Us</a></li>
                                <li> <a href="#Properties">Properties</a></li>
                                <li> <a href="#Contact">Contact</a></li>
                            </ul>
                        </div>
                        <div style="padding-top: 16px;">
                            <form action="/login" method="get">
                                <button class="header-buttan">Log in</button>
                            </form>
                        </div>
                    </header>
                    <main class="main">
                        <h1 class="title">Find Your Drem House</h1>
                        <p class="text-mainblock">Lorem ipsum dolor sit amet consectetur, adipisicing elit. Sed laudantium
                            odio,</br> fuga facilis quibusdam et molestias illo.</p>
                        <div class="section-block">
                            <div class="info">
                                <select class="drop-dawn">
                                    
                                    <option value="Location">Location</option>
                                </select>
                                <h2>California</h2>
                            </div>
                            <div class="info">
                                <select class="drop-dawn">
                                    <option value="Properties">Properties</option>
                                </select>
                                <h2>Delux</h2>
                            </div>
                            <div class="info">
                                <select class="drop-dawn">
                                    <option value="Prise">Price</option>
                                </select>
                                <h2>$10,000-$12,0000</h2>
                            </div>
                            <div>
                                <form action="https://www.tripadvisor.com/Hotels-g28926-c3-zff22-California-Hotels.html">
                                    <button class="search-btn">Search</button>
                                </form>
                            </div>
                        </div>
                    </main>
                    <div class="container-decor">
                        <div class="img-duo">
                            <img src="/static/imgrs/Rectangle 2257.png" alt="">
                            <img class="img-two" src="/static/imgrs/Rectangle 2258.png" alt="">
                        </div>
                        <div>
                            <div>
                                <h3 class="subtitle-about_us">About Us</h3>
                                <h2 class="subtitle-h2">We are Specializing in <br> interior Improvments</h2>
                                <p class="text-block_three">Lorem ipsum dolor sit amet, consectetur adipiscing <br> elit. Ut viverra
                                    posuere sem purus enim eleifend <br> habitant arcu, sed.</p>
                            </div>
                            <div>
                                <div class="mini-block_three">
                                    <div>
                                        <img style="margin-bottom: 24px;" src="/static/imgrs/support 1.png" alt="">
                                        <h3 class="mini-block_h3">Free Consulatation</h3>
                                        <p class="mini-block_text">Lorem ipsum dolor sit amet, <br> conse
                                            ctetur adipiscing elit.</p>
                                    </div>
                                    <div>
                                        <img style="margin-bottom: 24px;" src="/static/imgrs/team 1.png" alt="">
                                        <h3 class="mini-block_h3">Best Team Members</h3>
                                        <p class="mini block_text">Lorem ipsum dolor sit amet, conse <br>
                                            ctetur adipiscing elit.</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="color">
                        <h2 class="subtitle-looking">What are you looking for?</h2>
                        <div style="display: flex;">
                            <div>
                                <img class="img-four" src="/static/imgrs/Rectangle 2181.png" alt="">
                            </div>
                            <div class="color2">
                                <div class="block-4">
                                    <div>
                                        <img src="/static/imgrs/house (3) 1.png" alt="">
                                    </div>
                                    <div class="block-5">
                                        <h3>Family House</h3>
                                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing <br>elit. In tempor pulvinar at augue
                                            vestibulum euismod risus </p>
                                    </div>
                                </div>
                                <div class="block-4">
                                    <div>
                                        <img src="/static/imgrs/appartment 1.png" alt="">
                                    </div>
                                    <div class="block-5">
                                        <h3>
                                            Apartment
                                        </h3>
                                        <p>
                                            Lorem ipsum dolor sit amet, consectetur adipiscing <br> elit. In tempor pulvinar at
                                            augue vestibulum euismod <br> risus
                                        </p>
                                    </div>
                                </div>
                                <div class="block-4">
                                    <div>
                                        <img src="/static/imgrs/Group 3252.png" alt="">
                                    </div>
                                    <div class="block-5">
                                        <h3>
                                            Studio & Offices
                                        </h3>
                                        <p>
                                            Lorem ipsum dolor sit amet, consectetur adipiscing <br> elit. In tempor pulvinar at
                                            augue vestibulum euismod <br> risus
                                        </p>
                                    </div>
                                </div>
                                <div class="block-4">
                                    <div>
                                        <img src="/static/imgrs/Group 3253.png" alt="">
                                    </div>
                                    <div class="block-5">
                                        <h3>
                                            Villa & Condo
                                        </h3>
                                        <p>
                                            Lorem ipsum dolor sit amet, consectetur adipiscing <br> elit. In tempor pulvinar at
                                            augue vestibulum euismod <br> risus
                                        </p>
            
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="color-2">
                        <div>
                            <h2 class="Who-Choose-Us">
                                Who Choose Us?
                            </h2>
                            <p class="Lorem">
                                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Odio laoreet sit <br>
                                neque sagittis. Gravida viverra at auctor sed aliquam. Sed magna eros <br>
                                lectus amet, viverra. Ultrices diam, volutpat sit ut feugiat semper <br>
                                interdum dapibus. Et malesuada tempus lacus at ornare gravida ornare <br>
                                nulla dui. Velit tellus elit consectetur dui vel convallis eu in lectus. Vitae <br>
                                id est, suspendisse suspendisse.
                            </p>
                        </div>
                        <div>
                            <img class="istockphoto" src="/static/imgrs/istockphoto-1033381730-612x612-removebg-preview 1.png" alt="">
                        </div>
                    </div>
                    <div style="padding: 0px 150px;">
                        <div class="blue">
                            <h2 class="Daily">
                                For Daily Update Subscribe Now
                            </h2>
                            <div style="display: flex; position: relative;">
                                <input type="text" placeholder="Enter Your Mail..">
                                <button class="button-2">Subcribe</button>
                            </div>
                        </div>
                        <div class="logo-home_2">
                            <div>
                                <div class="logo-home_ class">
                                    <img src="/static/imgrs/Group 3311.png" alt="">
                                    <p style="padding-top: 16px;">Building</p>
                                </div>
                                <div>
                                    <p class="ipsum">
                                        Lorem ipsum dolor sit amet, consectet <br>
                                        adipiscing elit. Quam turpis sed ut fam <br>
                                        tortor pharetra. Lorem auctor congue <br>
                                        pellentesque facilisis diam
                                    </p>
                                </div>
                                <div class="Twitter" id="Properties">
                                    <img src="/static/imgrs/Facebook.png" alt="">
                                    <img class="Facebook" src="/static/imgrs/Twitter.png" alt="">
                                    <img class="Facebook" src="/static/imgrs/Group 3263.png" alt="">
                                    <img class="Facebook" src="/static/imgrs/Linked In.png" alt="">
                                </div>
                            </div>
                            <div class="Home">
                                <div class="Process">
                                    <ul style="list-style: none;">
                                        <li>
                                            <h2 id="Home">Home</h2>
                                        </li>
                                        <li class="sit">Process</li>
                                        <li class="site">Listing</li>
                                        <li class="site">Popular Property</li>
                                        <li class="site">Out Agents</li>
                                        <li class="site">Testimonial</li>
                                    </ul>
                                </div>
                                <div class="Process">
                                    <ul style="list-style: none;">
                                        <li>
                                            <h2 id="Service">Servies</h2>
                                        </li>
                                        <li class="sit">Site map</li>
                                        <li class="site">Property type</li>
                                        <li class="site">Terms and conditions</li>
                                        <li class="site">Privacy policy</li>
                                    </ul>
                                </div>
                                <div class="Process">
                                    <ul style="list-style: none;">
                                        <li>
                                            <h2 id="About">About</h2>
                                        </li>
                                        <li class="sit">About us</li>
                                        <li class="site">Who choose us?</li>
                                        <li class="site">Events</li>
                                        <li class="site">Blog</li>
                                    </ul>
                                </div>
                                <div class="Process">
                                    <ul style="list-style: none;">
                                        <li>
                                            <h2 id="Contact">Contact</h2>
                                        </li>
                                        <li class="sit">+888 561 258</li>
                                        <li class="site">webmaile@gmail.com</li>
                                        <li class="site">Google play</li>
                                    </ul>
                                </div>
                            </div>
            
                        </div>
                        <div>
                            <p class="Lorem"></p>
                        </div> 
                    </div>
                </div>
            </body>
            </html>"""
    
@app.route('/login', methods=['GET', 'POST'])
def b():
        if request.method == "POST":
            email_login = request.form.get('email')
            password_login = request.form.get('password')
            if email_login in div:
                if div[email_login] == password_login:
                    return redirect('/')
        return """<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Log in</title>
                <link rel="stylesheet" href="static/login.css">
            </head>
            <body>
                <main class="main">
                    <div class="global_div">
                        <div class="avatar">
                            <img src="static/imgrs/Group 3311.png" alt="" class="img_avatar">
                            <p class="img_text">Building</p>
                        </div>
                        <div class="Log_in">
                            <div class="login_text">
                                <h2>Log in</h2>
                            </div>
                            <div class="input_login">
                                <form action="/login" method="POST">
                                    <input type="text" name="email" placeholder="Enter Your Mail..">
                                    <br>
                                    <input type="text" name="password" placeholder="Password">
                                    <br>
                                    <button class="button_login">Log in</button>
                                </form>
                            </div>
                            <div class="New_account">
                                <p class="new_account_text">Need a account?</p>
                                <form action="/singin" method="get">
                                    <button class="new_account_button">Sing in</button>
                                </form>
                            </div>
                        </div>
                    </div>
                </main>
            </body>
            </html>"""
    
@app.route("/singin", methods=['GET', 'POST'])
def s():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        if email and password:
            if email not in div:
                div[email] = password
                return redirect('/login')
    return """<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Sing in</title>
                <link rel="stylesheet" href="static/Singin.css">
            </head>
            <body>
                <main class="main">
                    <div class="global_div">
                        <div class="avatar">
                            <img src="static/imgrs/Group 3311.png" alt="" class="img_avatar">
                            <p class="img_text">Building</p>
                        </div>
                        <div class="Log_in">
                            <div class="login_text">
                                <h2>Sing in</h2>
                            </div>
                            <div class="input_login">
                                <form action="/singin" method="POST">
                                    <input type="text" placeholder="Your Name">
                                    <br>              
                                    <input type="date" placeholder="Date of Birth">
                                    <br>
                                    <input type="text" name="email" placeholder="Enter Your Mail..">
                                    <br>
                                    <input type="text" name="password" placeholder="Password">
                                    <br>
                                <button class="button_login" type="submit">Sing in</button>
                                </form>

                            </div>
                        </div>
                    </div>
                </main>
            </body>
            </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
