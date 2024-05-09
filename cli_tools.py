import argparse
import importlib
import os
import sys
import traceback

# Tool metadata
TOOLS_METADATA = {
    'python': {
        'tools': ['hello_world', ' calculator'],
        'description': 'Python tools'
    },
    'javascript': {
        'tools': ['hello_world', 'string_utils'],
        'description': 'JavaScript tools'
    }
}

# Tool discovery and loading
def discover_tools(language):
    tools_dir = f'tools/{language}'
    tools = []
    for file in os.listdir(tools_dir):
        if file.endswith(f'.{language}'):
            tool_name = file[:-len(f'.{language}')]
            tools.append(tool_name)
    return tools

def load_tool(language, tool_name):
    module_name = f'tools.{language}.{tool_name}'
    try:
        module = importlib.import_module(module_name)
        return module
    except ImportError:
        print(f"Error: Tool '{tool_name}' not found for language '{language}'")
        sys.exit(1)

# Command-line argument parsing
def parse_args():
    parser = argparse.ArgumentParser(description='CLI tool collection')
    parser.add_argument('language', choices=TOOLS_METADATA.keys(), help='Programming language')
    parser.add_argument('tool', help='Tool name')
    parser.add_argument('args', nargs='*', help='Tool arguments')
    return parser.parse_args()

# Tool execution and output handling
def execute_tool(tool, args):
    try:
        output = tool.main(args)
        print(output)
    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()

# Error handling and debugging
def handle_error(e):
    print(f"Error: {e}")
    traceback.print_exc()

# Main entry point
def main():
    args = parse_args()
    language = args.language
    tool_name = args.tool
    tool_args = args.args

    tools = discover_tools(language)
    if tool_name not in tools:
        print(f"Error: Tool '{tool_name}' not found for language '{language}'")
        sys.exit(1)

    tool_module = load_tool(language, tool_name)
    execute_tool(tool_module, tool_args)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        handle_error(e)
