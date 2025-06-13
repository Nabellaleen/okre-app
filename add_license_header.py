#!/usr/bin/env python3

# Copyright (C) 2025  Florian Briand (Digital Engine)
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import subprocess

LICENSE_HEADER = """Copyright (C) 2025  Florian Briand (Digital Engine)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

COPYRIGHT = "Copyright (C) 2025  Florian Briand (Digital Engine)"
LICENSE_HEADER_PYTHON = '\n'.join(f'# {line}'.strip() for line in LICENSE_HEADER.split('\n'))
LICENSE_HEADER_HTML = f'<!--\n{LICENSE_HEADER}-->'

def add_license_to_file(file_path):
    # Determine the file type based on the extension
    if file_path.endswith('.py'):
        header = LICENSE_HEADER_PYTHON
    elif file_path.endswith('.html'):
        header = LICENSE_HEADER_HTML
    else:
        print(f"Unsupported file type: {file_path}")
        return

    # Read the existing content of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Check if the header is already present
    if COPYRIGHT in content:
        print(f"Header already present in {file_path}")
        return

    # Add the header at the beginning of the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(header + '\n\n' + content)
        print(f"Header added to {file_path}")


def get_versioned_files():
    try:
        # Use `git ls-files` to get tracked files
        result = subprocess.run(
            ["git", "ls-files", "*.py", "*.html"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        # Return the list of tracked Python files
        return result.stdout.strip().split("\n")
    except subprocess.CalledProcessError as e:
        print(f"Error running git ls-files: {e.stderr}")
        return []


if __name__ == "__main__":
    # Get versioned Python files
    python_files = get_versioned_files()
    for file_path in python_files:
        if file_path:  # Ensure the path is not empty
            add_license_to_file(file_path)
