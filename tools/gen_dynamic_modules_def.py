import re
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: gen_dynamic_modules_def.py <input_header> <output_def>")
        sys.exit(1)

    input_header = sys.argv[1]
    output_def = sys.argv[2]

    with open(input_header, 'r') as f:
        content = f.read()

    # Find all function declarations starting with envoy_dynamic_module_callback_
    # We assume they look like "void envoy_dynamic_module_callback_foo(...);"
    # The regex captures the function name.
    # We look for the return type (void or others), whitespace, then the function name.
    # Based on abi.h, they seem to be mostly void, but let's be generic.
    # Example: void envoy_dynamic_module_callback_http_get_header(
    matches = re.findall(r'\b(envoy_dynamic_module_callback_\w+)\(', content)

    # Remove duplicates and sort
    symbols = sorted(list(set(matches)))

    with open(output_def, 'w') as f:
        f.write("EXPORTS\n")
        for symbol in symbols:
            f.write(f"    {symbol}\n")

if __name__ == "__main__":
    main()
