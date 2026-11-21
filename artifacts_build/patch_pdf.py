with open("artifacts_build/generate_ieee_documentation.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
skip = False
for i, line in enumerate(lines):
    if '# Clean text for XML parsing in ReportLab' in line:
        skip = True
        new_lines.append('        # Safe XML escaping for ReportLab\n')
        new_lines.append('        clean_text = stripped.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")\n')
        new_lines.append('        # Convert markdown bold\n')
        new_lines.append('        parts = clean_text.split("**")\n')
        new_lines.append('        if len(parts) > 1:\n')
        new_lines.append('            res = []\n')
        new_lines.append('            for idx, part in enumerate(parts):\n')
        new_lines.append('                if idx % 2 == 1:\n')
        new_lines.append('                    res.append(f"<b>{part}</b>")\n')
        new_lines.append('                else:\n')
        new_lines.append('                    res.append(part)\n')
        new_lines.append('            clean_text = "".join(res)\n')
        new_lines.append('        try:\n')
        new_lines.append('            story.append(Paragraph(clean_text, body_style))\n')
        new_lines.append('        except Exception:\n')
        new_lines.append('            safe_fallback = stripped.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")\n')
        new_lines.append('            story.append(Paragraph(safe_fallback, body_style))\n')
    elif skip and 'story.append(Paragraph(clean_text, body_style))' in line:
        skip = False
    elif not skip:
        new_lines.append(line)

with open("artifacts_build/generate_ieee_documentation.py", "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("Patch applied successfully!")
