import re
import json
from engine import EligibilityEngine
import schemes_data

def test_presets():
    # Read index.html to extract preset keys
    with open('templates/index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Extract all data-preset attributes
    chip_presets = re.findall(r'data-preset="([^"]+)"', html)
    print(f"Found {len(chip_presets)} chip presets: {chip_presets}")

    # Extract all option values from presetStateSelect
    select_match = re.search(r'<select id="presetStateSelect"[^>]*>(.*?)</select>', html, re.DOTALL)
    assert select_match, "presetStateSelect not found in index.html"
    select_html = select_match.group(1)
    option_presets = re.findall(r'<option value="([^"]+)"', select_html)
    print(f"Found {len(option_presets)} option presets in select dropdown: {option_presets}")

    # Read app.js to extract PRESETS
    with open('static/js/app.js', 'r', encoding='utf-8') as f:
        js = f.read()

    # Extract PRESETS block
    presets_match = re.search(r'const PRESETS = (\{.*?\n\};)', js, re.DOTALL)
    assert presets_match, "PRESETS not found in app.js"
    presets_block = presets_match.group(1)

    # Check that all chip presets and option presets are in PRESETS block
    all_needed = set(chip_presets + option_presets)
    for p in all_needed:
        assert f'{p}:' in presets_block, f"Preset '{p}' missing from app.js PRESETS"

    print(f"All {len(all_needed)} preset keys exist in app.js PRESETS!")

    # Now let's test evaluation against backend for each state
    schemes = schemes_data.get_all_schemes()
    print(f"Total schemes in DB: {len(schemes)}")
    engine = EligibilityEngine(schemes=schemes)

    # Test all presets extracted from JS
    # We can extract the preset objects using regex
    pattern = r'(\w+):\s*\{\s*state:\s*"([^"]+)",\s*income:\s*(\d+),\s*category:\s*"([^"]+)",\s*marks:\s*(\d+),\s*gender:\s*"([^"]+)",\s*course_level:\s*"([^"]+)"'
    matches = re.findall(pattern, presets_block)
    print(f"\nExtracted {len(matches)} full preset definitions from app.js:")
    
    assert len(matches) == 37, f"Expected 37 presets, got {len(matches)}"

    for key, state, income, cat, marks, gender, course in matches:
        prof = {
            "state": state,
            "income": int(income),
            "category": cat,
            "marks": int(marks),
            "gender": gender,
            "course_level": course
        }
        results = engine.evaluate_profile(prof)
        eligible = [r for r in results if r.get("eligible")]
        assert len(eligible) > 0, f"No schemes for preset {key} ({state})"
        print(f"  ✓ [{key}] {state:35} -> {len(eligible)} eligible schemes")

    print(f"\nALL {len(matches)} INDIAN STATES & UT PRESETS EVALUATED AND PASS WITH 100% SUCCESS!")

if __name__ == '__main__':
    test_presets()
