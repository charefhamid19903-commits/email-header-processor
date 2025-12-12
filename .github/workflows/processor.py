#!/usr/bin/env python3
"""
Email Header Processor
Processes email headers by:
1. Removing specified lines
2. Changing domain 'fin' to '[RDNS]' in From field
3. Adding '[EID]' to Message-ID field
"""

import re
import sys
import argparse
from pathlib import Path

class EmailHeaderProcessor:
    def __init__(self):
        self.lines_to_remove = [
            'received',
            'return-path',
            'dkim-signature',
            'arc-seal',
            'arc-authentication-results',
            'arc-message-signature',
            'authentication-results',
            'x-google-dkim-signature',
            'x-gm-message-state'
        ]
    
    def process(self, header_text):
        """Process the email header"""
        lines = header_text.split('\n')
        processed_lines = []
        
        for line in lines:
            if not line.strip():
                processed_lines.append(line)
                continue
                
            # Check if line should be removed
            should_remove = False
            for pattern in self.lines_to_remove:
                if line.lower().startswith(pattern + ':'):
                    should_remove = True
                    break
            
            if should_remove:
                continue
            
            # Process From field
            if line.lower().startswith('from:'):
                line = self._process_from_line(line)
            
            # Process Message-ID field
            elif line.lower().startswith('message-id:'):
                line = self._process_message_id(line)
            
            processed_lines.append(line)
        
        return '\n'.join(processed_lines)
    
    def _process_from_line(self, line):
        """Change domain .fin to .[RDNS] in From field"""
        # Handle different formats
        # Format 1: From: name@domain.fin
        # Format 2: From: Name <name@domain.fin>
        line = re.sub(
            r'@([^\s>]+\.)fin([>\s]|$)',
            r'@\1[RDNS]\2',
            line,
            flags=re.IGNORECASE
        )
        return line
    
    def _process_message_id(self, line):
        """Add [EID] to Message-ID"""
        # If it has angle brackets
        if '<' in line and '>' in line:
            line = line.replace('>', '[EID]>')
        else:
            # Append [EID] at the end
            line = line.rstrip() + '[EID]'
        return line

def main():
    parser = argparse.ArgumentParser(description='Process email headers')
    parser.add_argument('-i', '--input', help='Input file with email header')
    parser.add_argument('-o', '--output', help='Output file (optional)')
    parser.add_argument('--clipboard', action='store_true', help='Copy to clipboard (requires pyperclip)')
    
    args = parser.parse_args()
    
    processor = EmailHeaderProcessor()
    
    # Read input
    if args.input:
        with open(args.input, 'r') as f:
            header = f.read()
    elif not sys.stdin.isatty():
        # Read from stdin
        header = sys.stdin.read()
    else:
        # Interactive mode
        print("Paste email header (Ctrl+D or Ctrl+Z to finish):")
        header_lines = []
        try:
            while True:
                line = input()
                header_lines.append(line)
        except EOFError:
            pass
        header = '\n'.join(header_lines)
    
    if not header.strip():
        print("No input provided!")
        sys.exit(1)
    
    # Process header
    processed = processor.process(header)
    
    # Output
    if args.output:
        with open(args.output, 'w') as f:
            f.write(processed)
        print(f"Processed header saved to {args.output}")
    else:
        print("\n" + "="*60)
        print("PROCESSED EMAIL HEADER:")
        print("="*60)
        print(processed)
    
    # Copy to clipboard if requested
    if args.clipboard:
        try:
            import pyperclip
            pyperclip.copy(processed)
            print("\n✓ Copied to clipboard!")
        except ImportError:
            print("\n⚠ Install pyperclip for clipboard support:")
            print("  pip install pyperclip")

if __name__ == "__main__":
    main()
