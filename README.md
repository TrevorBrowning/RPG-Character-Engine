# RPG Character Engine

This project is a Python-based character loader for a custom tabletop RPG system.

It parses a character sheet stored as a CSV file and converts it into a structured Python dictionary that can be reused across multiple tools such as character viewers, inventory systems, simulations, and (eventually) a GUI.

The goal is to build a clean, extensible foundation rather than a one-off script.

---

## Current Features

- Loads a character sheet from a CSV file
- Uses the first row as dynamic headers 
- Accumulates character data into lists per field
- Safely handles uneven rows and missing values
- Clean separation between:
  - file loading
  - data parsing
  - presentation logic (in progress)

---

## Project Structure

rpg-character-engine/
│
├── character.csv # Character sheet data
├── main.py # Core loader logic
├── README.md
└── presentations/ # Display layers (in progress)

---

## Design Philosophy

- **Data-driven**: The CSV defines the structure, not the code
- **Separation of concerns**: Parsing, presentation, and future game logic are kept separate
- **Future-proof**: Designed to support expansion without rewriting core systems
- **Readable first**: Prioritizes clarity over cleverness

---

## Planned Features / Future Work

- Presentation layers:
  - Simple view (core character info)
  - Extended view (skills, inventory, equipment)
  - Full debug view (all character data)
- Export character data to JSON
- Global item / weapon database (separate from character sheets)
- Inventory and stat calculations
- NPC and multi-character support
- GUI-based character viewer (Tkinter or web-based)

---

## Status

This project is actively being developed as a learning-focused but production-minded system.  
Core character loading is complete and stable; presentation layers are the next phase.

---

## Notes

This project intentionally avoids hardcoding RPG rules or mechanics at this stage.
Those systems will be layered on later once the data model is finalized.
