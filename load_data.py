import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skill_project.settings')
django.setup()

from analyzer.models import SkillData

def generate_major_project_data():
    print("🧹 Clearing database for a fresh start...")
    SkillData.objects.all().delete()

    # --- THE 300 SKILLS LIST ---
    
    # 1. Emerging (High Growth) - 100 Skills
    emerging = [
        "Generative AI", "LLM Ops", "Prompt Engineering", "Vector Databases", "LangChain", "PyTorch", "HuggingFace",
        "Stable Diffusion", "AutoGPT", "Web3", "Solidity", "Rust Programming", "Move Language", "Quantum Computing",
        "Edge AI", "TinyML", "Cybersecurity Mesh", "Zero Trust Architecture", "Next.js 14", "Tailwind CSS",
        "HTMX", "SvelteKit", "Bun Runtime", "Deno", "GoLang", "Kotlin Multiplatform", "SwiftUI", "Dart",
        "Snowflake Data Cloud", "Databricks", "Terraform", "Pulumi", "GitHub Actions", "ArgoCD", "Service Mesh",
        "ebpf", "Graph Databases", "Neo4j", "Pinecone", "Milvus", "PostgreSQL Vector", "Supabase", "Pocketbase",
        "Flutter", "React Native", "WebAssembly", "Blazor", "Micro-frontends", "Serverless Functions", "TRPC",
        "GraphQL Federation", "Apollo Client", "Prisma ORM", "Drizzle ORM", "PlanetScale", "CockroachDB",
        "Machine Learning Operations", "Data Engineering", "Feature Stores", "AI Ethics Compliance", "Reinforcement Learning",
        "Computer Vision", "NLP", "GANs", "Transformers Architecture", "Vision Transformers", "Diffusion Models",
        "Low-code AI", "No-code Automation", "Zapier Engineering", "Robotic Process Automation", "UiPath", "Blue Prism",
        "Digital Twins", "Industrial IoT", "5G Network Slicing", "Wi-Fi 7 Protocols", "Cloud-Native Security", 
        "Kubernetes Security", "DevSecOps", "SRE", "Observability", "Prometheus", "Grafana", "OpenTelemetry",
        "Chaos Engineering", "Gremlin", "FinOps", "Cloud Cost Optimization", "Green Computing", "Sustainable IT",
        "Bio-computing", "Neuromorphic Computing", "Autonomous Systems", "Drone Programming", "V2X Communication",
        "Spatial Computing", "Apple VisionOS", "Unity Engine", "Unreal Engine 5", "Metaverse Development"
    ]

    # 2. Stable (Mainstream/Steady) - 100 Skills
    stable = [
        "Python", "Java", "JavaScript", "C#", "C++", "SQL", "HTML5", "CSS3", "PHP", "Ruby", "TypeScript",
        "React", "Angular", "Vue.js", "Node.js", "Express.js", "Django", "Flask", "Spring Boot", "Laravel",
        "ASP.NET Core", "Ruby on Rails", "MySQL", "PostgreSQL", "MongoDB", "Oracle DB", "Microsoft SQL Server",
        "Redis", "Elasticsearch", "Linux Administration", "Shell Scripting", "Bash", "PowerShell", "Git",
        "Docker", "Kubernetes", "AWS", "Azure", "Google Cloud Platform", "Firebase", "Heroku", "Jenkins",
        "Maven", "Gradle", "NPM", "Yarn", "Webpack", "Vite", "Bootstrap", "Sass", "LESS", "Redux", "Context API",
        "REST API", "JSON", "XML", "SOAP", "OAuth 2.0", "JWT", "Unit Testing", "Jest", "JUnit", "Selenium",
        "Cypress", "Postman", "Agile Methodology", "Scrum", "Kanban", "Jira", "Confluence", "Microservices",
        "Monolithic Architecture", "Event-Driven Design", "Message Queues", "RabbitMQ", "Apache Kafka",
        "ETL Processes", "Data Warehousing", "Business Intelligence", "Tableau", "Power BI", "Excel VBA",
        "Wordpress", "Shopify", "Magento", "Web Security", "Penetration Testing", "Encryption", "VPC",
        "Load Balancing", "DNS Management", "Active Directory", "Virtualization", "VMware", "VirtualBox",
        "UI Design", "UX Design", "Figma", "Adobe XD", "Mobile Web Design", "Progressive Web Apps"
    ]

    # 3. Declining (Legacy/Obsolescence) - 100 Skills
    declining = [
        "jQuery", "Adobe Flash", "ActionScript", "Silverlight", "VB6", "VBScript", "Pascal", "COBOL", "Fortran",
        "Perl", "Delphi", "ColdFusion", "Apache Struts 1", "EJB 2.0", "SVN", "Mercurial", "CVS", "CoffeeScript",
        "XSLT", "XPath", "SOAP API", "WSDL", "Apache Ant", "Bower", "Gulp", "Grunt", "Backbone.js", "Knockout.js",
        "AngularJS 1.x", "MooTools", "Prototype.js", "YUI Library", "ExtJS", "Sencha Touch", "Symbian OS",
        "Blackberry OS", "Windows Phone Development", "Cordova", "PhoneGap", "Sencha", "Internet Explorer 11",
        "Netscape", "FrontPage", "Dreamweaver", "FTP Uploading", "Marquee Tags", "Table-based Layouts",
        "Flash Animation", "Shockwave", "RealPlayer", "Winamp Plugins", "ActiveX", "Applets", "XHTML",
        "WAP/WML", "Objective-C", "PowerBuilder", "FoxPro", "Clipper", "Paradox DB", "Lotus Notes",
        "AS400", "Mainframe Assembly", "Punch Card Systems", "Floppy Disk Drivers", "Dial-up Protocols",
        "NetBEUI", "IPX/SPX", "Gopher", "Telnet", "RSH", "WML Script", "Compact Framework", "Silverlight",
        "XNA Framework", "MOTO-DEV", "PalmOS", "Tizen (Mobile)", "FirefoxOS", "Ubuntu Touch", "J2ME",
        "Brew MP", "MeeGo", "Bada", "Maemo", "Blackberry Cascades", "WebOS", "Grid Layout (Old)",
        "Framesets", "Image Maps", "Java Web Start", "CORBA", "DCOM", "RMI", "Enterprise Service Bus (Legacy)",
        "BizTalk (Old Versions)", "Crystal Reports 8", "UML Modeling (Heavy)", "Rational Rose"
    ]

    years = [2023, 2024, 2025]
    
    def seed_category(skill_list, trend):
        for name in skill_list:
            # Random starting point for job postings
            base = random.randint(5000, 80000)
            for year in years:
                if trend == "emerging":
                    # Upward trend: 30% to 50% growth
                    factor = 1 + (random.uniform(0.3, 0.5) * (year - 2022))
                elif trend == "declining":
                    # Downward trend: 20% to 40% loss
                    factor = 1 - (random.uniform(0.2, 0.4) * (year - 2022))
                else:
                    # Stable: +/- 5% variance
                    factor = 1 + random.uniform(-0.05, 0.05)
                
                postings = int(base * factor)
                # Demand score is loosely correlated with trend
                d_score = random.randint(70, 99) if trend == "emerging" else random.randint(10, 40) if trend == "declining" else random.randint(45, 75)
                
                SkillData.objects.create(
                    skill_name=name,
                    year=year,
                    job_postings=max(postings, 50),
                    demand_score=d_score
                )
        print(f"✅ Imported 100 {trend} skills.")

    seed_category(emerging, "emerging")
    seed_category(stable, "stable")
    seed_category(declining, "declining")

    print(f"\n🚀 TOTAL: {SkillData.objects.count()} records for 300 skills loaded!")

if __name__ == "__main__":
    generate_major_project_data()