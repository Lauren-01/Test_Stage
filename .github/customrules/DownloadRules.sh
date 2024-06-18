#!/bin/bash

# Controleer of de vereiste omgevingsvariabelen zijn ingesteld
if [ -z "$JSON_FILE" ]; then
  echo "Error: JSON_FILE is not set."
  exit 1
fi

# Stel de basis-URL in voor de mappings
MAPPINGS_URL="https://github.com/aws-cloudformation/aws-guard-rules-registry/tree/main/mappings"

# Stel de basis-URL in voor de regels
RULES_URL="https://github.com/aws-cloudformation/aws-guard-rules-registry/tree/main/rules/aws"

# Controleer of de download map bestaat, zo niet, maak deze aan
RULES_DIR=".github/customrules/downloaded_rulesets"

# Download het JSON-bestand van de opgegeven URL
curl -o "$MAPPINGS_URL/$JSON_FILE"

# Controleer of het bestand correct is gedownload
if [ ! -s "$JSON_FILE" ]; then
  echo "Failed to download $JSON_FILE or the file is empty."
  exit 1
fi

# Verwijder eventuele regels die er nog in stonden zodat de nieuwe enkel getest worden
rm $RULES_DIR/*

# Gebruik jq om de regels te extraheren en download de individuele regels
jq -r '.mappings[]?.guardFilePath' "$JSON_FILE" | while read -r rule; do
  rule_url="$RULES_URL/$rule"
  local_rule_path="$RULES_DIR/$(basename $rule)"
  echo "Downloading $local_rule_path from $rule_url"
  curl -s -o "$local_rule_path" "$rule_url"
  # Controleer of het bestand correct is gedownload
  if [ ! -s "$local_rule_path" ]; then
    echo "Failed to download $local_rule_path or the file is empty."
    exit 1
  fi
done

echo "All rules downloaded successfully."
