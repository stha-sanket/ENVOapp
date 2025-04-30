# Environmental quiz questions with options, correct answers, and explanations

quiz_questions = [
    {
        "question": "Which of the following is NOT a renewable energy source?",
        "options": ["Solar", "Wind", "Natural Gas", "Hydroelectric"],
        "correct_answer": 2,
        "explanation": "Natural gas is a fossil fuel and is not renewable. Solar, wind, and hydroelectric are all renewable energy sources."
    },
    {
        "question": "What percentage of the Earth's water is available as fresh water for human use?",
        "options": ["About 50%", "About 25%", "Less than 1%", "About 10%"],
        "correct_answer": 2,
        "explanation": "Less than 1% of Earth's water is available as fresh water for human use. Most water (97%) is in oceans, and much of the remaining fresh water is locked in ice caps and glaciers."
    },
    {
        "question": "Which practice helps reduce food waste?",
        "options": ["Meal planning", "Buying in bulk regardless of need", "Ignoring expiration dates", "Refrigerating all produce"],
        "correct_answer": 0,
        "explanation": "Meal planning helps you buy only what you need, reducing food waste. Buying in bulk without a plan can lead to waste, and not all produce should be refrigerated."
    },
    {
        "question": "What is the primary cause of ocean acidification?",
        "options": ["Agricultural runoff", "Plastic pollution", "Carbon dioxide absorption", "Oil spills"],
        "correct_answer": 2,
        "explanation": "Ocean acidification occurs primarily when the ocean absorbs carbon dioxide from the atmosphere, creating carbonic acid and lowering the pH of seawater."
    },
    {
        "question": "Which of these actions would most reduce your carbon footprint?",
        "options": ["Eating less meat", "Using paper instead of plastic", "Buying new energy-efficient appliances", "Washing clothes in cold water"],
        "correct_answer": 0,
        "explanation": "Reducing meat consumption, especially beef, has one of the largest impacts on reducing your carbon footprint due to the high emissions associated with livestock production."
    },
    {
        "question": "What is the greenhouse effect?",
        "options": ["Plants growing in enclosed glass structures", "Heat trapped by gases in the atmosphere", "Morning dew on grass", "Fog in valleys"],
        "correct_answer": 1,
        "explanation": "The greenhouse effect is the process where gases in the atmosphere (like CO2 and methane) trap heat from the sun, warming the Earth. Without it, Earth would be too cold for life, but excess greenhouse gases are causing dangerous warming."
    },
    {
        "question": "Which of the following is the largest contributor to plastic pollution in oceans?",
        "options": ["Fishing nets and equipment", "Plastic straws", "Plastic bottles", "Microbeads from cosmetics"],
        "correct_answer": 0,
        "explanation": "Fishing gear, including nets and equipment, makes up about 46% of the Great Pacific Garbage Patch. While all plastic waste is problematic, abandoned fishing equipment is the largest contributor to ocean plastic."
    },
    {
        "question": "What does the term 'biodiversity' refer to?",
        "options": ["The variety of plant and animal life in a habitat", "The process of composting organic material", "The study of human impacts on nature", "A sustainable farming technique"],
        "correct_answer": 0,
        "explanation": "Biodiversity refers to the variety of living species in a given area, including plants, animals, and microorganisms. High biodiversity is essential for ecosystem resilience and stability."
    },
    {
        "question": "What is 'fast fashion'?",
        "options": ["Quick-drying synthetic fabrics", "Clothing designed for athletes", "Inexpensive clothing produced rapidly to follow trends", "Automated garment production"],
        "correct_answer": 2,
        "explanation": "Fast fashion refers to inexpensive clothing produced rapidly to meet the latest trends, typically with short wear cycles. This industry has significant environmental impacts, including high water usage, chemical pollution, and textile waste."
    },
    {
        "question": "Which of these countries has the highest per capita carbon emissions?",
        "options": ["China", "United States", "India", "Russia"],
        "correct_answer": 1,
        "explanation": "While China has the highest total carbon emissions, the United States has significantly higher per capita emissions. This means the average American produces more carbon dioxide than the average Chinese citizen."
    },
    {
        "question": "What is the main cause of deforestation in tropical rainforests?",
        "options": ["Logging for timber", "Agricultural expansion", "Urban development", "Climate change"],
        "correct_answer": 1,
        "explanation": "Agricultural expansion, including cattle ranching and crop production (particularly soy and palm oil), is the primary driver of tropical deforestation. Logging, mining, and infrastructure development also contribute."
    },
    {
        "question": "Which transportation method typically has the lowest carbon footprint per person per mile?",
        "options": ["Flying", "Driving alone", "Taking a train", "Taking a cruise ship"],
        "correct_answer": 2,
        "explanation": "Trains, especially electric ones, typically have the lowest carbon emissions per passenger-mile. Flying and cruise ships are among the most carbon-intensive forms of transportation."
    },
    {
        "question": "What is 'greenwashing'?",
        "options": ["A technique for cleaning with eco-friendly products", "Marketing that misleadingly suggests products are environmentally friendly", "Painting buildings green to reduce heat absorption", "Growing plants on building facades"],
        "correct_answer": 1,
        "explanation": "Greenwashing is when companies make misleading environmental claims about their products or practices to appear more environmentally responsible than they actually are."
    },
    {
        "question": "Which of the following is considered a 'keystone species'?",
        "options": ["Invasive species", "Endangered species", "Species that have a disproportionate effect on their environment", "Species that can survive in multiple environments"],
        "correct_answer": 2,
        "explanation": "Keystone species have a disproportionately large effect on their environment relative to their abundance. Examples include sea otters, wolves, and bees. Their removal can cause significant ecosystem changes."
    },
    {
        "question": "What is 'eutrophication' in aquatic ecosystems?",
        "options": ["Excessive nutrient enrichment leading to algal blooms", "Water purification through natural filtration", "Loss of water due to evaporation", "Freezing of surface water in winter"],
        "correct_answer": 0,
        "explanation": "Eutrophication occurs when bodies of water receive excessive nutrients (often from fertilizer runoff or sewage), causing algal blooms. These blooms can deplete oxygen and create 'dead zones' where aquatic life cannot survive."
    },
    {
        "question": "Which of the following best defines 'carbon neutrality'?",
        "options": ["Eliminating all carbon emissions", "Having a net zero carbon footprint", "Using only renewable energy", "Planting trees to absorb CO2"],
        "correct_answer": 1,
        "explanation": "Carbon neutrality means having a net zero carbon footprint by balancing carbon emissions with carbon removal or simply eliminating carbon emissions altogether. This can involve reducing emissions and offsetting remaining emissions."
    },
    {
        "question": "Which of these is NOT a common component of household recycling programs?",
        "options": ["Paper and cardboard", "Glass containers", "Plastic packaging", "Disposable diapers"],
        "correct_answer": 3,
        "explanation": "Disposable diapers typically cannot be recycled in household recycling programs due to contamination and their complex material composition. They usually end up in landfills where they can take hundreds of years to decompose."
    },
    {
        "question": "What is the primary environmental concern with electronic waste (e-waste)?",
        "options": ["It takes up too much space in landfills", "It contains toxic materials that can leach into soil and water", "It's difficult to transport", "It generates heat in landfills"],
        "correct_answer": 1,
        "explanation": "Electronic waste contains toxic materials like lead, mercury, and cadmium that can leach into soil and groundwater if not properly disposed of. Additionally, valuable materials that could be recycled are lost when e-waste goes to landfills."
    },
    {
        "question": "Which of the following is an example of a 'circular economy' practice?",
        "options": ["Disposing of products after a single use", "Manufacturing products designed to be reused or recycled", "Increasing production efficiency to make more products", "Converting forests to agricultural land"],
        "correct_answer": 1,
        "explanation": "A circular economy aims to minimize waste by designing products to be reused, repaired, remanufactured, or recycled, rather than disposed of after use. This approach contrasts with the traditional 'take-make-dispose' linear economy."
    },
    {
        "question": "What does the term 'food miles' refer to?",
        "options": ["The distance food travels from farm to consumer", "The rate at which food decomposes", "The calories contained in various foods", "The efficiency of food production"],
        "correct_answer": 0,
        "explanation": "Food miles measure the distance food travels from where it's produced to where it's consumed. Lower food miles generally indicate less fuel used for transportation and potentially fresher food, though production methods can have an even larger environmental impact."
    }
]
