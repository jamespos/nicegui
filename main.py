from nicegui import ui
import os

position = 'Freelance Photographer'
name = 'Sarah Richards'
email_address = 'sarah.richards@freelancephoto.com'
date = 2024

@ui.page('/')
def home():
    ui.add_head_html('''
    <style>
        .banner-image {
            height: 300px;
            width: 100%;
            border: none;
            padding: 0;
            margin: 0;
        }
        .header_title {
            font-weight: bold;
            font-size: 40px;
            font-family: Harrington;
            text-shadow: 2px 2px;
            font-style: italic;
        }
        .footer-image {
            height: 80px;
            width: 100%;
            border: none;
            padding: 0;
            margin: 0;
        }
    </style>
    ''')

    with ui.interactive_image('pics/fixedImg/picture.jpg').classes('banner-image'):
        ui.column().style('position: relative; display: inline-block;')
        ui.image(
            'pics/fixedImg/profile.jpg').style('border-radius: 50%; width: 150px; height: 150px; position: absolute; top: 60px; left: 50px;')
        with ui.grid(columns=2):
            ui.html('<strong>Name:</strong> ').style('position: absolute; top: 60px; left: 250px;')
            ui.html(f'<strong>{name}</strong> ').style('position: absolute; top: 60px; left: 400px;')
            ui.html('<strong>Current position:</strong ').style('position: absolute; top: 80px; left: 250px;')
            ui.html(f'<strong>{position}</strong ').style('position: absolute; top: 80px; left: 400px;')
            ui.html('<strong>Email Address:</strong> ').style('position: absolute; top: 100px; left: 250px;')
            ui.html(f'<strong>{email_address}</strong> ').style('position: absolute; top: 100px; left: 400px;')

    navigation = ui.row()
    ui.link_target('about_me')
    ui.link_target('qualifications')
    ui.link_target('pictures')
    ui.link_target('experience')

    ui.label('About Me').classes('header_title')

    with ui.card():
        ui.label('About Me:')
        ui.label('Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the '
                 'industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type '
                 'and scrambled it to make a type specimen book. It has survived not only five centuries, but also the '
                 'leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s '
                 'with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop '
                 'publishing software like Aldus PageMaker including versions of Lorem Ipsum.'
                 'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of '
                 'classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin '
                 'professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, '
                 'consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical '
                 'iterature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 '
                 'f "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This '
                 'book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of '
                 'Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.'
                 'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of '
                 'classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin '
                 'professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, '
                 'consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical '
                 'literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 '
                 'of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. T'
                 'his book is a treatise on the theory of ethics, very popular during the Renaissance. The first '
                 'line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.')

    ui.label('Qualifications').classes('header_title')
    with ui.card():
        ui.label('Qualifications:')
        ui.label('Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the '
                 'industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type '
                 'and scrambled it to make a type specimen book. It has survived not only five centuries, but also the '
                 'leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s '
                 'with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop '
                 'publishing software like Aldus PageMaker including versions of Lorem Ipsum.'
                 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the '
                 'industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type '
                 'and scrambled it to make a type specimen book. It has survived not only five centuries, but also the '
                 'leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s '
                 'with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop '
                 'publishing software like Aldus PageMaker including versions of Lorem Ipsum.'
                 'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of '
                 'classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin '
                 'professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, '
                 'consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical '
                 'iterature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 '
                 'f "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This '
                 'book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of '
                 'Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.'
                 'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of '
                 'classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin '
                 'professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, '
                 'consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical '
                 'literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 '
                 'of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. T'
                 'his book is a treatise on the theory of ethics, very popular during the Renaissance. The first '
                 'line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.')

    ui.label('Experience').classes('header_title')
    with ui.card():
        ui.label('Experience:')
        ui.label('Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the '
                 'industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type '
                 'and scrambled it to make a type specimen book. It has survived not only five centuries, but also the '
                 'leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s '
                 'with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop '
                 'publishing software like Aldus PageMaker including versions of Lorem Ipsum.'
                 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the '
                 'industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type '
                 'and scrambled it to make a type specimen book. It has survived not only five centuries, but also the '
                 'leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s '
                 'with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop '
                 'publishing software like Aldus PageMaker including versions of Lorem Ipsum.'
                 'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of '
                 'classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin '
                 'professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, '
                 'consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical '
                 'iterature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 '
                 'f "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This '
                 'book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of '
                 'Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.'
                 'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of '
                 'classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin '
                 'professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, '
                 'consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical '
                 'literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 '
                 'of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. T'
                 'his book is a treatise on the theory of ethics, very popular during the Renaissance. The first '
                 'line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.'
                 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the '
                 'industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type '
                 'and scrambled it to make a type specimen book. It has survived not only five centuries, but also the '
                 'leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s '
                 'with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop '
                 'publishing software like Aldus PageMaker including versions of Lorem Ipsum.'
                 'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of '
                 'classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin '
                 'professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, '
                 'consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical '
                 'iterature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 '
                 'f "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This '
                 'book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of '
                 'Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.'
                 'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of '
                 'classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin '
                 'professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, '
                 'consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical '
                 'literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 '
                 'of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. T'
                 'his book is a treatise on the theory of ethics, very popular during the Renaissance. The first '
                 'line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.')
    with navigation:
        ui.link('About Me', '#about_me')
        ui.link('Qualifications', '#qualifications')
        ui.link('Experience', '#experience')
        ui.link('All Pictures', all_pictures)

    with ui.footer().classes('footer-image'):
        ui.interactive_image('pics/fixedImg/picture.jpg')
        with ui.element('div').style('position: absolute; top: 50%; left: 90%; transform: translate(-50%, -50%);'):
            # Add icons over the image
            with ui.link('Facebook', 'https://www.facebook.com'):
                ui.icon('facebook').style('margin: 0 10px; font-size: 30px; color: blue')
        with ui.element('div').style('position: absolute; top: 50%; left: 80%; transform: translate(-50%, -50%);'):
            # Add icons over the image
            with ui.link('Instagram', 'https://www.instagram.com'):
                ui.image('pics/icons/instagram.png').style('margin: 0 10px; height: 25px; width: 25px')
        with ui.element('div').style('position: absolute; top: 50%; left: 70%; transform: translate(-50%, -50%);'):
            # Add icons over the image
            with ui.link('LinkedIn', 'https://www.linkedIn.com'):
                ui.image('pics/icons/linkedin.png').style('margin: 0 10px; height: 25px; width: 25px')

        with ui.element('div').style('position: absolute; top: 50%; right: 75%; transform: translate(-50%, -50%);'):
            ui.label(f'© {date} {name}. All Rights Reserved.').style('color: black')


@ui.page('/all_pictures')
def all_pictures():
    ui.add_head_html('''
        <style>
            .banner-image {
                height: 300px;
                width: 100%;
                border: none;
                padding: 0;
                margin: 0;
            }
            .all_pic_title {
                font-weight: bold;
                font-size: 40px;
                font-family: Harrington;
                text-align: center;
                text-shadow: 2px 2px;
                font-style: italic;
            }
            .footer-image {
                height: 80px;
                width: 100%;
                border: none;
                padding: 0;
                margin: 0;
            }
        </style>
        ''')

    with ui.interactive_image('pics/fixedImg/picture.jpg').classes('banner-image'):
        ui.column().style('position: relative; display: inline-block;')
        ui.image('pics/fixedImg/profile.jpg').style(
            'border-radius: 50%; width: 150px; height: 150px; position: absolute; top: 60px; left: 50px;')
        with ui.grid(columns=2):
            ui.html('<strong>Name:</strong> ').style('position: absolute; top: 60px; left: 250px;')
            ui.html(f'<strong>{name}</strong> ').style('position: absolute; top: 60px; left: 400px;')
            ui.html('<strong>Current position:</strong ').style('position: absolute; top: 80px; left: 250px;')
            ui.html(f'<strong>{position}</strong ').style('position: absolute; top: 80px; left: 400px;')
            ui.html('<strong>Email Address:</strong> ').style('position: absolute; top: 100px; left: 250px;')
            ui.html(f'<strong>{email_address}</strong> ').style('position: absolute; top: 100px; left: 400px;')

    with ui.row():
        ui.link('Home', home)
        ui.link('All Pictures', all_pictures)
        ui.link('Profile Pics', profile_pictures)
        ui.link('Landscape Pics', landscape_pictures)

    ui.label('All Pictures').classes('all_pic_title')

    image_folder = 'pics/profile'
    with ui.row().classes('grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 lg:grid-cols-6 xl:grid-cols-8 gap-4'):
        for image_name in os.listdir(image_folder):
            with ui.column().classes('flex items-center justify-center'):
                if image_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                    ui.space().style('width: 10px')
                    image_path = os.path.join(image_folder, image_name)
                    ui.image(image_path).style('width: 200px; height: 200px;')

    image_folder = 'pics/landscape'
    with ui.row().classes('grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 lg:grid-cols-6 xl:grid-cols-8 gap-4'):
        for image_name in os.listdir(image_folder):
            with ui.column().classes('flex items-center justify-center'):
                if image_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                    ui.space().style('width: 10px')
                    image_path = os.path.join(image_folder, image_name)
                    ui.image(image_path).style('width: 200px; height: 200px;')

    with ui.footer().classes('footer-image'):
        ui.interactive_image('pics/fixedImg/picture.jpg')
        with ui.element('div').style('position: absolute; top: 50%; left: 90%; transform: translate(-50%, -50%);'):
            # Add icons over the image
            with ui.link('Facebook', 'https://www.facebook.com'):
                ui.icon('facebook').style('margin: 0 10px; font-size: 30px; color: blue')
        with ui.element('div').style('position: absolute; top: 50%; left: 80%; transform: translate(-50%, -50%);'):
            # Add icons over the image
            with ui.link('Instagram', 'https://www.instagram.com'):
                ui.image('pics/icons/instagram.png').style('margin: 0 10px; height: 25px; width: 25px')
        with ui.element('div').style('position: absolute; top: 50%; left: 70%; transform: translate(-50%, -50%);'):
            # Add icons over the image
            with ui.link('LinkedIn', 'https://www.linkedIn.com'):
                ui.image('pics/icons/linkedin.png').style('margin: 0 10px; height: 25px; width: 25px')

        with ui.element('div').style('position: absolute; top: 50%; right: 75%; transform: translate(-50%, -50%);'):
            ui.label(f'© {date} {name}. All Rights Reserved.').style('color: black')


@ui.page('/profile_pictures')
def profile_pictures():
    ui.add_head_html('''
            <style>
                .banner-image {
                    height: 300px;
                    width: 100%;
                    border: none;
                    padding: 0;
                    margin: 0;
                }
                .header_title {
                    font-weight: bold;
                    font-size: 40px;
                    font-family: Harrington;
                    text-align: center;
                    text-shadow: 2px 2px;
                    font-style: italic;
                }
                .footer-image {
                    height: 80px;
                    width: 100%;
                    border: none;
                    padding: 0;
                    margin: 0;
                }
            </style>
            ''')

    with ui.interactive_image('pics/fixedImg/picture.jpg').classes('banner-image'):
        ui.column().style('position: relative; display: inline-block;')
        ui.image('pics/fixedImg/profile.jpg').style(
            'border-radius: 50%; width: 150px; height: 150px; position: absolute; top: 60px; left: 50px;')
        with ui.grid(columns=2):
            ui.html('<strong>Name:</strong> ').style('position: absolute; top: 60px; left: 250px;')
            ui.html(f'<strong>{name}</strong> ').style('position: absolute; top: 60px; left: 400px;')
            ui.html('<strong>Current position:</strong ').style('position: absolute; top: 80px; left: 250px;')
            ui.html(f'<strong>{position}</strong ').style('position: absolute; top: 80px; left: 400px;')
            ui.html('<strong>Email Address:</strong> ').style('position: absolute; top: 100px; left: 250px;')
            ui.html(f'<strong>{email_address}</strong> ').style('position: absolute; top: 100px; left: 400px;')

    with ui.row():
        ui.link('Home', home)
        ui.link('All Pictures', all_pictures)
        ui.link('Profile Pics', profile_pictures)
        ui.link('Landscape Pics', landscape_pictures)

    ui.label('Profile Pictures').classes('header_title')

    image_folder = 'pics/profile'
    with ui.row().classes('grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 lg:grid-cols-6 xl:grid-cols-8 gap-4'):
        for image_name in os.listdir(image_folder):
            with ui.column().classes('flex items-center justify-center'):
                if image_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                    ui.space().style('width: 10px')
                    image_path = os.path.join(image_folder, image_name)
                    ui.image(image_path).style('width: 200px; height: 200px;')

    with ui.footer().classes('footer-image'):
        ui.interactive_image('pics/fixedImg/picture.jpg')
        with ui.element('div').style('position: absolute; top: 50%; left: 90%; transform: translate(-50%, -50%);'):
            # Add icons over the image
            with ui.link('Facebook', 'https://www.facebook.com'):
                ui.icon('facebook').style('margin: 0 10px; font-size: 30px; color: blue')
        with ui.element('div').style('position: absolute; top: 50%; left: 80%; transform: translate(-50%, -50%);'):
            # Add icons over the image
            with ui.link('Instagram', 'https://www.instagram.com'):
                ui.image('pics/icons/instagram.png').style('margin: 0 10px; height: 25px; width: 25px')
        with ui.element('div').style('position: absolute; top: 50%; left: 70%; transform: translate(-50%, -50%);'):
            # Add icons over the image
            with ui.link('LinkedIn', 'https://www.linkedIn.com'):
                ui.image('pics/icons/linkedin.png').style('margin: 0 10px; height: 25px; width: 25px')

        with ui.element('div').style('position: absolute; top: 50%; right: 75%; transform: translate(-50%, -50%);'):
            ui.label(f'© {date} {name}. All Rights Reserved.').style('color: black')


@ui.page('/landscape_pictures')
def landscape_pictures():
    ui.add_head_html('''
                <style>
                    .banner-image {
                        height: 300px;
                        width: 100%;
                        border: none;
                        padding: 0;
                        margin: 0;
                    }
                    .header_title {
                        text-align: center;
                        font-weight: bold;
                        font-size: 40px;
                        font-family: Harrington;
                        text-shadow: 2px 2px;
                        font-style: italic;
                    }
                    .footer-image {
                        height: 80px;
                        width: 100%;
                        border: none;
                        padding: 0;
                        margin: 0;
                    }
                </style>
                ''')

    with ui.interactive_image('pics/fixedImg/picture.jpg').classes('banner-image'):
        ui.column().style('position: relative; display: inline-block;')
        ui.image('pics/fixedImg/profile.jpg').style(
            'border-radius: 50%; width: 150px; height: 150px; position: absolute; top: 60px; left: 50px;')
        with ui.grid(columns=2):
            ui.html('<strong>Name:</strong> ').style('position: absolute; top: 60px; left: 250px;')
            ui.html(f'<strong>{name}</strong> ').style('position: absolute; top: 60px; left: 400px;')
            ui.html('<strong>Current position:</strong ').style('position: absolute; top: 80px; left: 250px;')
            ui.html(f'<strong>{position}</strong ').style('position: absolute; top: 80px; left: 400px;')
            ui.html('<strong>Email Address:</strong> ').style('position: absolute; top: 100px; left: 250px;')
            ui.html(f'<strong>{email_address}</strong> ').style('position: absolute; top: 100px; left: 400px;')

    with ui.row():
        ui.link('Home', home)
        ui.link('All Pictures', all_pictures)
        ui.link('Profile Pics', profile_pictures)
        ui.link('Landscape Pics', landscape_pictures)

    ui.label('Landscape Pictures').classes('header_title')

    image_folder = 'pics/landscape'

    with ui.row().classes('grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 lg:grid-cols-6 xl:grid-cols-8 gap-4'):
        for image_name in os.listdir(image_folder):
            with ui.column().classes('flex items-center justify-center'):
                if image_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                    ui.space().style('width: 10px')
                    image_path = os.path.join(image_folder, image_name)
                    ui.image(image_path).style('width: 200px; height: 200px;')

    with ui.footer().classes('footer-image'):
        ui.interactive_image('pics/fixedImg/picture.jpg')
        with ui.element('div').style('position: absolute; top: 50%; left: 90%; transform: translate(-50%, -50%);'):
            # Add icons over the image
            with ui.link('Facebook', 'https://www.facebook.com'):
                ui.icon('facebook').style('margin: 0 10px; font-size: 30px; color: blue')
        with ui.element('div').style('position: absolute; top: 50%; left: 80%; transform: translate(-50%, -50%);'):
            # Add icons over the image
            with ui.link('Instagram', 'https://www.instagram.com'):
                ui.image('pics/icons/instagram.png').style('margin: 0 10px; height: 25px; width: 25px')
        with ui.element('div').style('position: absolute; top: 50%; left: 70%; transform: translate(-50%, -50%);'):
            # Add icons over the image
            with ui.link('LinkedIn', 'https://www.linkedIn.com'):
                ui.image('pics/icons/linkedin.png').style('margin: 0 10px; height: 25px; width: 25px')

        with ui.element('div').style('position: absolute; top: 50%; right: 75%; transform: translate(-50%, -50%);'):
            ui.label(f'© {date} {name}. All Rights Reserved.').style('color: black')


ui.run()
