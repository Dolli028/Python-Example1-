import tkinter as tk
import random

#FIRST: Implement and test your Pokemon class below
class Pokemon:
    def __init__(self,species_name, dex_number, catch_rate, speed):
        self.species_name = species_name
        self.dex_number = dex_number
        self.catch_rate = catch_rate
        self.speed= speed
    def __str__(self):
        return str(self.species_name)
#NEXT: Complete the class definition provided below
class SafariSimulator(tk.Frame):
    def __init__(self, master=None):
        self.caught_list = []
        self.master = master
        self.safari_balls = 30
        self.pokemon_caught = 0 
        pokemon_ls =[]
        pokemon_dict = {}
        self.pokemon_dict = pokemon_dict
        fp = open('pokedex.csv')
        for line in fp:
            new_line = line.rstrip('\n')
            pokemon_ls.append(new_line)
        for string in pokemon_ls:
            new_string = string.split(',')
            Pokemon_name = str(Pokemon(new_string[1],new_string[0],new_string[2],new_string[3]))
            pokemon_dict[Pokemon_name] = new_string[0],new_string[2],new_string[3]
        del pokemon_dict['Pokemon']
        fp.close 
        #Read in the data file from pokedex.csv at some point here
        #It's up to you how you store and handle the data 
        #(e.g., list, dictionary, etc.),
        #but you must use your Pokemon class in some capacity

        #Initialize any instance variables you want to keep track of

        #DO NOT MODIFY: These lines set window parameters and create widgets
        tk.Frame.__init__(self, master)
        master.minsize(width=275, height=350)
        master.maxsize(width=275, height=350)
        master.title("Safari Zone Simulator")
        self.pack()
        self.createWidgets()
        self.nextPokemon()

        #Call nextPokemon() method here to initialize your first random pokemon

    def createWidgets(self):
        self.throwButton = tk.Button(self)
        self.throwButton["text"]="Throw Safari Ball("+str(30)+"left)"
        self.throwButton["command"] = self.throwBall
        self.throwButton.pack()
        #See the image in the instructions for the general layout required
        #"Run Away" button has been completed for you as an example:
        self.runButton = tk.Button(self)
        self.runButton["text"] = "Run Away"
        self.runButton["command"] = self.nextPokemon
        self.runButton.pack()
        

        #You need to create two additional labels:

        
        self.messageLabel = tk.Label(bg="grey")
        self.messageLabel.pack(fill="x")
        self.messageLabel['text'] ='You encounter a wild bulbasaur'
        #Complete and pack the pokemonImageLabel here.
        self.pokemonImageLabel = tk.Label()
        self.pokemonImageLabel.pack()
        dex_number = 1
        pokemon_number = ('sprites/'+str(dex_number)+'.gif')
        self.photo = tk.PhotoImage(file = pokemon_number)
        self.pokemonImageLabel['image'] = self.photo
        
        #Complete and pack the catchProbLabel here.
        self.catchProbLabel = tk.Label(bg="grey")
        self.catchProbLabel.pack(fill="x")
        self.catchProbLabel['text']='Your chance of catching it is 33%'
    def nextPokemon(self):
        new_pokemon=(random.choice(list(self.pokemon_dict.items())))
        self.messageLabel['text'] ='You encounter a wild '+str(new_pokemon[0])
        dex_number = new_pokemon[1][0]
        self.species_name = new_pokemon[0]
        self.catch_rate = new_pokemon[1][1]
        pokemon_number = ('sprites/'+str(dex_number)+'.gif')
        self.photo = tk.PhotoImage(file = pokemon_number)
        self.pokemonImageLabel['image'] = self.photo
        catch_percent = int((min(int(new_pokemon[1][1]),151)/449.5)*100)
        self.catchProbLabel['text']='Your chance of catching it is '+str(catch_percent)+'%!'
        
        #This method must:
            #Choose a random pokemon
            #Get the info for the appropriate pokemon
            #Ensure text in messageLabel and catchProbLabel matches the pokemon
            #Change the pokemonImageLabel to show the right pokemon

        #Hint: to see how to create an image, look at the documentation 
        #for the PhotoImage/Label classes in tkinter.
        
        #Once you generate a PhotoImage object, it can be displayed 
        #by setting self.pokemonImageLabel["image"] to it
        
        #Note: the PhotoImage object MUST be stored as an instance
        #variable for some object (you can just set it to self.photo).
        #Not doing this will, for weird memory reasons, cause the image 
        #to not be displayed.
        
    def throwBall(self):
        self.safari_balls -=1
        self.throwButton["text"]="Throw Safari Ball("+str(self.safari_balls)+"left)"
        chance = random.random()
        chance_of_catch= (min(int(self.catch_rate),151)/449.5)
        
        if chance_of_catch> chance:
            self.caught_list.append(self.species_name )
            self.nextPokemon()
        else:
            self.messageLabel['text'] ="Aargh! It escaped!"
        if self.safari_balls <= 0:
            self.endAdventure()
        
        #This method must:

            #Decrement the number of balls remaining
            #Try to catch the pokemon
            #Check to see if endAdventure() should be called

        #To determine whether or not a pokemon is caught, generate a random
        #number between 0 and 1, using random.random().  If this number is
        #less than min((catchRate+1), 151) / 449.5, then it is caught. 
        #catchRate is the integer in the Catch Rate column in pokedex.csv, 
        #for whatever pokemon is being targetted.
        
        #Don't forget to update the throwButton's text to reflect one 
        #less Safari Ball (even if the pokemon is not caught, it still 
        #wastes a ball).
        
        #If the pokemon is not caught, you must change the messageLabel
        #text to "Aargh! It escaped!"
        
        #Don't forget to call nextPokemon to generate a new pokemon 
        #if this one is caught.
        
    def endAdventure(self):
        self.runButton.pack_forget()
        self.throwButton.pack_forget()
        self.messageLabel.pack_forget()
        self.pokemonImageLabel.pack_forget()
        self.catchProbLabel.pack_forget()
        self.endLabel=tk.Label(bg="grey")
        self.endLabel.pack(fill="x")
        self.endLabel['text'] = "You're all out of balls, hope you had fun!"
        self.PokemonCaught = tk.Label(bg = "grey")
        self.PokemonCaught.pack(fill="x")
        self.PokemonCaught['text'] = 'you caught ' +  str(len(self.caught_list))+' Pokemon:'
        for item in self.caught_list:
            n=0
            self.n = tk.Label(bg = "grey")
            self.n.pack(fill ="x")
            self.n['text'] = str(item)
            n+=1
            
            
        #This method must: 

            #Display adventure completion message
            #List captured pokemon

        #Hint: to remove a widget from the layout, you can call the 
        #pack_forget() method.
        
        #For example, self.pokemonImageLabel.pack_forget() removes 
        #the pokemon image.




#DO NOT MODIFY: These lines start your app
app = SafariSimulator(tk.Tk())
app.mainloop()
