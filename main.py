import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def parse_command(argv):
    args = []
    flags = []
    for arg in argv:
        if arg.startswith("--"):
            flags.append(arg)
        else:
            args.append(arg)
    return args, flags

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    verbose = False
    
    args, flags = parse_command(sys.argv[1:])

    prompt = " ".join(args)
    
    if "--verbose" in flags:
        verbose = True
        print(f"User prompt: {prompt}")

    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]

    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)
    print(response.text)

    if verbose:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
