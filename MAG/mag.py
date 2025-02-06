# ======================================== #
bold = '\033[1m'
italic = '\033[3m'
strike = '\033[9m'
underline = '\033[4m'
dim = '\033[2m'

reset = '\033[0m'

red = '\033[31m'
green = '\033[32m'
blue = '\033[34m'
cyan = '\033[36m'
yellow = '\033[33m'
magenta = '\033[35m'

# More colors (using RGB escape codes)
orange = '\033[38;2;255;165;0m'  
teal = '\033[38;2;0;128;128m'    
peach = '\033[38;2;255;218;185m' 
cream = '\033[38;2;250;240;230m' 
forest_green = '\033[38;2;34;139;34m' 
burgundy = '\033[38;2;128;0;32m'
light_gray = '\033[38;2;200;200;200m' 
dark_gray = '\033[38;2;100;100;100m' 
olive = '\033[38;2;128;128;0m' 

# Background colors (using RGB escape codes)
bg_light_gray = '\033[48;2;200;200;200m' # Light Gray background
bg_orange = '\033[48;2;255;165;0m'  # Orange background
# ======================================== #

import random
import os

month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
year_range = [2019, 2020, 2021, 2022, 2024, 2025]
titles = [
    "The Majestic Whales: Giants of the Ocean",
    "Exploring the Depths: A Journey into the Abyss",
    "The Enigmatic World of Quantum Physics",
    "Artificial Intelligence: The Future of Humanity?",
    "The Art of Bonsai: Miniature Landscapes in Your Home",
    "The Culinary Delights of Italian Cuisine",
    "A Beginner's Guide to Astronomy",
    "The Wonders of the Amazon Rainforest",
    "The History of Ancient Egypt",
    "The Impact of Social Media on Society",
    "The Benefits of Regular Exercise",
    "The Importance of Environmental Conservation",
    "The Magic of Music: How it Affects Our Brains",
    "The Rise and Fall of the Roman Empire",
    "The Beauty of Nature Photography",
    "The Science of Sleep: Understanding its Importance",
    "The World of Cryptocurrency",
    "The Art of Public Speaking",
    "The Power of Positive Thinking",
    "The Secrets of Successful Investing",
    "The History of the Internet",
    "The Future of Space Exploration",
    "The Importance of Education",
    "The Art of Creative Writing",
    "The Science of Climate Change",
    "The Benefits of Meditation",
    "The World of Virtual Reality",
    "The Impact of Technology on Healthcare",
    "The Importance of Cultural Diversity",
    "The Future of Transportation",
    "The Art of Leadership",
    "The Science of Happiness",
    "The World of Robotics",
    "The Impact of Globalization",
    "The Importance of Critical Thinking",
    "The Future of Work",
    "The Art of Negotiation",
    "The Science of Learning",
    "The World of Biotechnology",
    "The Impact of Pandemics",
    "The Importance of Financial Literacy",
    "The Future of Energy",
    "The Art of Storytelling",
    "The Science of Nutrition",
    "The World of Nanotechnology",
    "The Impact of Artificial Intelligence on Jobs",
    "The Importance of Mental Health",
    "The Future of Food",
    "The Art of Problem Solving",
    "The Science of Psychology",
    "The World of Cybersecurity",
    "The Impact of Automation",
    "The Importance of Ethics",
    "The Future of Education",
    "The Art of Persuasion",
    "The Science of Genetics",
    "The World of Renewable Energy",
    "The Impact of Big Data",
    "The Importance of Creativity",
    "The Future of Communication",
    "The Art of Design",
    "The Science of Materials",
    "The World of Space Travel",
    "The Impact of the Metaverse",
    "The Importance of Adaptability",
    "The Future of Healthcare",
    "The Art of Innovation",
    "The Science of Consciousness",
    "The World of Quantum Computing",
    "The Impact of Social Justice Movements",
    "The Importance of Global Citizenship",
    "The Future of Democracy",
    "The Art of Diplomacy",
    "The Science of Economics",
    "The World of Philosophy",
    "The Impact of Artificial General Intelligence",
    "The Importance of Self-Awareness",
    "The Future of Humanity",
    "The Art of Living a Meaningful Life",
    "The Science of Well-being",
    "The World of the Universe",
    "The Impact of the Singularity",
    "The Importance of Love",
    "The Future of Everything"  # Added one more to make it 70
]

tags = {
    "programming": [
        "Python",
        "JavaScript",
        "Java",
        "C++",
        "C#",
        "Go",
        "Swift",
        "Kotlin",
        "Ruby",
        "PHP",
        "TypeScript",
        "R",
        "Objective-C",
        "Assembly Language",  # Could be considered hardware-adjacent
        "Perl",
        "Scala",
        "Rust",
        "Dart",
        "Lua"
    ],
    "hardware": [
        "Verilog",
        "VHDL",
        "SystemVerilog",
        "Bluespec"
    ],
    "technical": [
        "UML",
        "Agile",
        "Scrum",
        "DevOps",
        "Cloud Computing",
        "Big Data",
        "Machine Learning",
        "Deep Learning",
        "Data Science",
        "Cybersecurity",
        "Networking",
        "Database Management",
        "Software Engineering",
        "Project Management",
        "IT Infrastructure",
        "Embedded Systems", # Hardware-software overlap
        "Computer Architecture",
        "Operating Systems"
    ],
    "software": [
        "Software Development",
        "Web Development",
        "Mobile App Development",
        "Game Development",
        "Frontend Development",
        "Backend Development",
        "Full-Stack Development",
        "Desktop Application Development",
        "Cloud Computing", # Overlaps with technical
        "Database Development",
        "API Development",
        "Testing",
        "Quality Assurance",
        "UI/UX Design"
    ]
}
used_dates = set()
used_titles = set()

def create_markdown(filesNum):
    for i in range(1, filesNum + 1):
        filename = f"post{i}.md"
        filepath = os.path.join(".", filename)

        while True:
            day = random.randint(1, 28)
            month = random.choice(month_names)
            year = random.choice(year_range)
            date_str = f"{day:02} {month} {year}"
            if date_str not in used_dates:
                used_dates.add(date_str)
                break

        while True:
            title = random.choice(titles)
            if title not in used_titles:
                used_titles.add(title)
                break
                
        num_tags = random.randint(3, 5)  # Randomly choose 3 to 5 tags
        selected_tags = []
        for _ in range(num_tags):
            category = random.choice(list(tags.keys()))
            tag = random.choice(tags[category])
            selected_tags.append(tag)
            
        with open(filepath, "w") as f:
            f.write("+++\n")
            f.write(f"date = '{date_str}'\n")
            f.write("draft = false\n")
            f.write(f"title = '{title}'\n")
            f.write(f"tags = {selected_tags}\n")
            f.write("+++\n\n")  # Add a newline after the frontmatter
            # You can add more content to the file here if you want
            # f.write("Your post content goes here...\n") # Example content

        print(f'Created {filename} with date: {date_str}, title: {title}, tags: {selected_tags}')


print('Welcome to the random post creator\n')
while True:
    posts = input("How many number of posts you want to create: ")
    if posts.isdigit():
        postsNo = int(posts)
        if postsNo < 71:  # Adjusted limit to avoid running out of titles
            create_markdown(postsNo)
            break
        else:
            print("\nPlease enter a valid number! Or enter 'q' to exit.\n")

    elif posts == 'q':
        exit()

    else:
        print("\nPlease enter a valid number! Or enter 'q' to exit.\n")
