from agents import Agent, Runner, function_tool
from dotenv import load_dotenv
import os
# Load the environment variables from the .env file
load_dotenv()

# Set the OpenAI API key from the environment variables
model = os.getenv("MODEL", 'gpt-4o-mini')

# Use the function_tool decorator to properly format your tool
@function_tool
def save_to_file(code: str) -> str:
    """
    Saves the provided Markdown format text to a file.
    
    Args:
        code (str): The Markdown formatted text to save
        
    Returns:
        str: Confirmation message
    """
    with open('recommendations.md', 'w') as file:
        file.write(code)
    return "Recommendations has been saved to recommendations.txt"

# Add an OpenAI Agent to gather software requirements
pulsar_agent = Agent(
    name="ApachePulsarSpecialist",
    instructions="""
    You are an Apache Pulsar specialist in setup and operations of Apache Pulsar. Your task is to write the Pulsar setup requirements and recommendations for the user request. 
    The requirements should be well researched and documented with footnotes from the web, and thoroughly explained, using the best practices 
    and guidelines for Apache Pulsar.
    You should include:
    1. The recommended # of Brokers and Bookies based on messages per second, number of consumers and producers, and message size
    2. Disk space requirement for storing messages as requested
    3. Retention policy for message deletion
    4. Node configuration for Brokers and Bookies, like CPUs, RAM, etc. 
    5. High availability and durability configuration
    6. Monitoring and performance tuning recommendations
    7. Any additional considerations or best practices
    8. Save the requirements to a file in Markdown format using the provided save_to_file function.
    """,
    model=model,
    tools=[save_to_file] # Add the save_to_file tool
)

def main():
    print(f"Sending Apache Pulsar requirements to {model} model...")

###############################################################################
### Update the user request below to your specific requirements
    req_result = Runner.run_sync(pulsar_agent, 
    """
    I need to process 50000 messages per second with Apache Pulsar.
    Each message is 1.5KB in size.
    I need to ensure high availability and durability of the Pulsar system. 
    Each message should be processed at least once, to 15 different consumers. 
    I need to store messages for 1 days and have a retention policy to delete messages after that period. 
    I also need to monitor the system for performance and errors.
    """)
###############################################################################

    print("Recommendations completed. See the \"recommendations.md\" file for the results and sizing info.")
    print(req_result.final_output)

if __name__ == "__main__":
    main()
