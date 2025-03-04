from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

JOBS = [
        {
            "id": 1,
            "title": "Software Engineer",
            "location": "New York, USA",
            "salary": "$120,000"
        },
        {
            "id": 2,
            "title": "Data Analyst",
            "location": "Toronto, Canada",
            "salary": "$85,000"
        },
        {
            "id": 3,
            "title": "Marketing Manager",
            "location": "London, UK",
            "salary": "£75,000"
        },
        {
            "id": 4,
            "title": "Product Designer",
            "location": "Berlin, Germany",
            "salary": "€70,000"
        },
        {
            "id": 5,
            "title": "Cybersecurity Specialist",
            "location": "San Francisco, USA",
            "salary": "$130,000"
        },
        {
            "id": 6,
            "title": "AI Research Scientist",
            "location": "Tokyo, Japan",
            "salary": "¥15,000,000"
        }
    ]

NEWS = [
    {
        "title": "Apple Unveils New AI-Powered MacBook",
        "summary": "Apple has introduced its latest MacBook lineup featuring AI-powered performance enhancements.",
        "key_highlights": [
            "New M3 chip with AI acceleration",
            "Longer battery life up to 20 hours",
            "Improved neural engine for machine learning tasks"
        ],
        "body": "Apple's latest MacBook lineup brings significant improvements in artificial intelligence processing. The newly designed M3 chip includes a dedicated neural engine that boosts AI-driven applications. With enhanced efficiency, the laptops offer longer battery life and faster processing speeds, making them ideal for professionals and content creators.",
        "conclusion": "The AI-powered MacBook represents a major step in integrating machine learning at the hardware level, setting a new standard for laptops."
    },
    {
        "title": "Stock Market Sees Sharp Decline Amid Inflation Concerns",
        "summary": "Global markets tumbled as investors react to rising inflation and interest rate hikes.",
        "key_highlights": [
            "Dow Jones drops by 500 points",
            "Tech stocks face the biggest losses",
            "Federal Reserve signals further interest rate hikes"
        ],
        "body": "Markets witnessed a sharp decline today as inflation fears continue to rattle investors. The Dow Jones fell by 500 points, with tech stocks being the hardest hit. The Federal Reserve has indicated the possibility of further interest rate hikes to combat inflation, adding to market uncertainty.",
        "conclusion": "With economic conditions remaining volatile, investors are advised to stay cautious and diversify their portfolios to minimize risks."
    },
    {
        "title": "OpenAI Announces GPT-5: The Future of AI",
        "summary": "OpenAI has officially announced the development of GPT-5, promising advanced reasoning and contextual understanding.",
        "key_highlights": [
            "Better contextual awareness in conversations",
            "Improved efficiency and reduced bias",
            "Potential applications in healthcare and finance"
        ],
        "body": "OpenAI has confirmed the development of GPT-5, the next-generation AI model set to surpass its predecessor in natural language understanding and decision-making. The company aims to enhance GPT-5’s contextual reasoning abilities, making it more reliable for real-world applications.",
        "conclusion": "The announcement of GPT-5 has generated excitement across industries, with expectations that it will drive innovation in multiple sectors."
    },
    {
        "title": "Bitcoin Surges Above $50,000 Amid Institutional Adoption",
        "summary": "Bitcoin reaches a new high as major financial institutions embrace cryptocurrency.",
        "key_highlights": [
            "Bitcoin crosses $50,000 for the first time in months",
            "Institutional investors increase crypto holdings",
            "SEC considers approval of Bitcoin ETFs"
        ],
        "body": "Bitcoin has once again surpassed the $50,000 mark as institutional investors continue to pour funds into the crypto market. The growing acceptance of Bitcoin ETFs and regulatory clarity has fueled the surge, with analysts predicting further gains.",
        "conclusion": "With mainstream adoption growing, Bitcoin could see even greater highs, though volatility remains a concern for investors."
    },
    {
        "title": "Tech Layoffs Continue as Companies Cut Costs",
        "summary": "Major tech firms announce job cuts amid economic downturn and restructuring efforts.",
        "key_highlights": [
            "Google, Amazon, and Meta lay off thousands of employees",
            "AI and automation impact traditional tech jobs",
            "Stock prices of tech giants remain under pressure"
        ],
        "body": "The technology sector is witnessing another wave of layoffs as companies attempt to streamline operations amid economic challenges. Google, Amazon, and Meta have announced workforce reductions to focus on AI-driven automation and cost-cutting measures.",
        "conclusion": "While layoffs may improve financial stability for companies, concerns about job security in the tech industry continue to rise."
    }
]



@app.route('/')
def index():
  return render_template('home.html', jobs = JOBS, news = NEWS, company_name = 'Kedia Capital')

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

if (__name__ == '__main__'):
  app.run(host = '0.0.0.0', port = 8080, debug = True)

# def hello_world():
#   return "Hello World!"

# print(hello_world())