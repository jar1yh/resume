#!/usr/bin/env python3
import zipfile
import xml.etree.ElementTree as ET
import os

# Change to the script directory
os.chdir('/Users/ram/Documents/GitHub/resume')

# DOCX files are ZIP archives containing XML
with zipfile.ZipFile('Ramkumar_Jaganathan.docx', 'r') as docx:
    # Read the document.xml which contains the main content
    xml_content = docx.read('word/document.xml')
    
    # Parse the XML
    root = ET.fromstring(xml_content)
    
    # Define namespaces
    namespaces = {
        'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
        'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
    }
    
    # Find all hyperlinks
    hyperlinks = root.findall('.//w:hyperlink', namespaces)
    
    # Also read the relationships file to get actual URLs
    rels_content = docx.read('word/_rels/document.xml.rels')
    rels_root = ET.fromstring(rels_content)
    
    rels_ns = {'r': 'http://schemas.openxmlformats.org/package/2006/relationships'}
    
    print("Hyperlinks found in the document:")
    print("=" * 80)
    
    # Create a map of relationship IDs to targets
    rel_map = {}
    for rel in rels_root.findall('.//r:Relationship', rels_ns):
        rel_map[rel.get('Id')] = rel.get('Target')
    
    # Print each hyperlink with its text
    for hyperlink in hyperlinks:
        rel_id = hyperlink.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')
        if rel_id and rel_id in rel_map:
            url = rel_map[rel_id]
            # Get the text content
            text_elements = hyperlink.findall('.//w:t', namespaces)
            text = ''.join([t.text for t in text_elements if t.text])
            print(f"Text: '{text}'")
            print(f"URL: {url}")
            print("-" * 80)
