"""
Test suite verifying evaluation across all 28 Indian States & 8 Union Territories.
"""

from app import app

client = app.test_client()

all_states = [
    'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh',
    'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka',
    'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram',
    'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu',
    'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal',
    'Andaman and Nicobar Islands', 'Chandigarh', 'Dadra and Nagar Haveli and Daman and Diu',
    'Delhi', 'Jammu and Kashmir', 'Ladakh', 'Lakshadweep', 'Puducherry', 'Pan-India'
]

passed = 0
for st in all_states:
    res = client.post('/api/evaluate', json={
        'state': st,
        'income': 100000,
        'category': 'SC',
        'course_level': 'UG',
        'marks': 85,
        'gender': 'Female'
    })
    data = res.get_json()
    matches = data.get('total_matches', 0)
    assert matches > 0, f"No schemes matched for {st}"
    passed += 1

print(f"PASS: Verified all {passed} States and Union Territories! Every state has matching schemes.")
