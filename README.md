<h1>Dictionary Search (and Synonym Check)</h1>
<h3>Intro</h3>
<p>Hello and welcome to the Chatting with Python course! This is the synonym checking project where you'll create a function that filters through a dictionary to see where the first two synonyms are located. Please feel free to use the <code>main.py</code> file for reference, and use these steps as your guide.</p>
<h3>How to reproduce this</h3>
<ol>
	<li>Create your own dictionary, or copy and paste the one listed in the <code>main.py</code> file</li>
	<li>Create a function and then make a <code>for</code> loop within this function that runs through all the keys of the dictionary</li>
    <li>Then add a temporary "key holder" variable that stores the value of a key so it can be called throughout the looping process. In this same step, make sure to create a "key index" variable so it can record at <b>which location</b> the first synonym was found. <b>This is important for three reasons</b>: 
    <ol>
        <li>Python dictionaries do not have an order, so you need to create one</li>
        <li>If you try to run this function without an index, it'll simply return the same key's value twice because it doesn't know that that's not the same key from before, and thus assumes it's a synonym</li>
        <ul>
            <li><b>If you're confused by this step, think of it this way</b>: when you walk your normal path to your house, you remember all the things you pass by on the way. A Python interpreter needs a path for its dictionaries laid out for it to remember where each piece of information is stored, and this is done through indexing. Without this path that helps you remember, you'd easily get lost and assume every house that looks like yours is, in fact, yours (if you had the mind of a computer, of course).</li>
        </ul>
        <li>We'll use this to compare it with the second key's value</li>
    </ol>
	<li>Create a second <code>for</code> loop within the first loop. This will be our "potential synonym" loop that checks for a potential second synonym</li>
    <li>Make sure to create an index for that "potential synonym" key</li>
    <li>Set a condition that checks if the keys' values are the same AND that their indices are different! (If both conditions true, return a statement showing your keys (the words that are synonymous); if false, return a statement saying you could not find any synonyms)</li>
</ol>
<h3>How to use it</h3>
<p>Simply run the file and let it find the synonyms for you. You can also choose to search the dictionary if you'd like. You can copy and paste your own dictionary (make sure it's named the same as listed in the file I've provided) to double check if you've got synonyms. Remember, this only checks for the <b>first</b> set (a pair, really) of synonyms.</p>