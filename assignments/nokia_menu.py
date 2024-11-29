print("Please choose a menu\n.Press\n.1.Phonebook\n.2.Messages\n.3.Chat\n.4.Call register\n.5.Tones\n.6.Settings\n.7.Call divert\n.8.Games\n.9.Calculator\n.10.Reminders\n.11.Clock\n.12.Profiles\n.13.Sim services\n")
answer=int(input('Enter an option: '))
match answer:
	case 1:
		print("1.Search\n.2.Service numbers\n.3.Add name\n.4.Erase\n.5.Edit\n.6.Assign tone\n.7.Send b'card\n.8.Options\n.9.Speed dials\n.10.Voice tags\n")
		phonebook=int(input('Enter an option: '))
		match phonebook:
			case 1: print("Search")
			case 2: print("Service numbers")
			case 3: print("Add name")
			case 4: print("Erase")
			case 5: print("Edit")
			case 6: print("Assign tone")
			case 7: print("Send b'card")
			case 8: print("Options")
			print("1.Type of view\n2.Memory status")
			options=int(input('Enter an option: ')) 
			match options:
				case 1: print("Type of view")
				case 2: print("Memory status")
			case 9: print("Speed dials")		
			case 10: print("Voice tags")

	case 2:
		print("1.Write messages\n2.Inbox\n3.Outbox\n4.Picture messages\n5.Templates\n6.Smileys\n7.Message settings\n8.Info service\n9.Voice mailbox number\n10.Service command editor\n")
		messages=int(input('Enter an option: ')) 
		match messages:
			case 1: print("Write messages")
			case 2: print("Inbox")
			case 3: print("Outbox")
			case 4: print("Picture messages")
			case 5: print("Tempelates")
			case 6: print("Smileys")
			case 7: print("Message settings")
			print("1.Set 1\n2.Common\n")
			messageSettings=int(input('Enter an option: ')) 
			match messageSettings:
				case 1: print("Set 1")
				set1=int(input('Enter an option: ')) 
				match set1:  
					case 1: print("Message center number")
					case 2: print("Message sent as")
					case 3: print("Message validity")
				case 2: print("Common")
				common=int(input('Enter an option: ')) 
				match common:  
					case 1: print("Delivery reports")
					case 2: print("Reply via same centre")
					case 3: print("Character support")
			case 8: print("Info service")
			case 9: print("Voice mailbox number") 
			case 10:print("Service command editor")

	case 3:
		print("Chat\n")
		chat=int(input('Enter an option: '))    
		match(chat):
			case 1: print("Chat")
	case 4:
		print("1.Missed calls\n2.Recieved calls\n3.Dialed number\n4.Erase recent call list\n5.Show call duration\n6.Show call cost\n7.Call cost settings\n8.Prepaid credit\n.")
		callRegister=int(input('Enter an option: ')) 
		match(callRegister):
			case 1: print("Missed calls")
			case 2: print("Recieved calls")
			case 3: print("Dialed numbers")
			case 4: print("Erase recent call lists")
			case 5: print("Show call duration")
			print("1.Last call duration\n2.All calls' duration\n4.Dialled calls' duration\n5.Clear timers\n")
			showCallDuration=int(input('Enter an option: '))
			match showCallDuration:  
				case 1: print("Last call duration")
				case 2: print("All calls duration")
				case 3: print("Recieved calls' duration")
				case 4: print("Dialled calls' duration")
				case 5: print("Clear timers")
			case 6: print("Show call cost")
			print("1.Last call cost\n2.All calls cost\n3.Clear counters\n.")
			showCallCost=int(input('Enter an option: ')) 
			match(showCallCost):
				case 1: print("Last call duration")
				case 2: print("All calls duration")
				case 3: print("Clear counters")
			case 7: print("Call cost settings")
			print("\ncall cost limit\n2.Delivery report\n")
			callCostSettings=int(input('Enter an option: ')) 
	     		match(callCostSettings):
				case 1: print("Call cost limit")
				case 2: print("Show cost in")
			case 8: print("Prepaid credit")

	case 5:
		print("1.Ringing tone\n2.Ringing volume\n3.Incoming call alert\n4.Composer\n5.Message alert tone\n6.Keypad tones\n7.Warning and game tones\n8.Vibrating alert\n9.Screen saver\n")
		tones=int(input('Enter an option: ')) 
		match tones:
			case 1: print("Ringing tone")
			case 2: print("Ringing volume")
			case 3: print("Incoming call alert")
			case 4: print("Composer")   
			case 5: print("Message alert tone")
			case 6: print("Keypad tones")
			case 7: print("Warning and game tones")
			case 8: print("Vibrating alert")
			case 9: print("Screen saver")

	case 6:
		print("1.Call settings\n2.Phone settings\n3.Security settings\n4.Restore factory settings\n")
		settings=int(input('Enter an option: ')) 
		match settings:  
			case 1:print("Call settings");
			print("1.Automatic redial\n2.Speed dialling\n3.Call waiting options\n4.Own number sending\n5.Phone line in use\n6.Automatic answer\n")
			callSettings=int(input('Enter an option: ')) 
			match callSettings  
				case 1:print("Automatic redial")
				case 2:print("Speed dialling")
				case 3:print("Call waiting options")
				case 4:print("Own number sending")
				case 5:print("Phone line in use")
				case 6:print("Automatic answer")
			case 2:print("Phone settings")
			print("1.Language\n2.Cell info display\n3.Welcome note\n4.Network selection\n5.Lights\n6.Confirm SIM service actions\n")
			phoneSettings=int(input('Enter an option: ')) 
			match phoneSettings:
				case 1:print("Language")
				case 2:print("Cell info display")
				case 3:print("Welcome note")
				case 4:print("Network selection")
				case 5:print("Lights")
				case 6:print("Confirm SIM service actions")
			case 3:print("Security settings")
			print("1.PIN code request\n2.Call barring service\n3.Fixed dialling\n4.Closed user group\n5.Phone security\n6.Change access codes\n")
			securitySettings=int(input('Enter an option: '))
			match securitySettings:
				case 1:print("PIN code request")
				case 2:print("Call barring service")
				case 3:print("Fixed dialling")
				case 4:print("Closed user group")
				case 5:print("Phone security")
				case 6:print("Change access codes")
			case 4:print("Restore factory settings\n")
			print("Restore factory settings\n")
			restoreFactorySettings=int(input('Enter an option))
			match restoreFactorySettings: 
				case 1:print("Restore factory settings")
   
	case 7:
		print("Call divert\n")
		callDivert=int(input('Enter an option)) 
		match callDivert:  
			case 1:print("Restore factory settings")

	case 8:print("Games\n")
		games=int(input('Enter an option'))
		match games:
			case 1:print("Games")     
			
	case 9:print("Calculator\n")
		calculator=int(input('Enter an option: '))
		match calculator:
			case 1:print("calculator")
			
	case 10:print("Reminders\n")
		reminders=int(input('Enter an option: '))
		match reminders
			case 1:print("reminders")
			
	case 11:print("Clock\n")
		print("1.Alarm clock\n2.Clock settings\n3.Date setting\n4.Stopwatch\n5.Countdown timer\n6.Auto update of date and time\n")
		clock=int(input('Enter an option: '))
		match clock:  
			case 1:print("Alarm clock")
			case 2:print("Clock settings")
			case 3:print("Date setting")
			case 4:print("Stopwatch")
			case 5:print("Countdown timer")
			case 6:print("Auto update of date and time")
			
	case 12: print("Profile")
		profile=int(input('Enter an option: '))
		match profile:
			case 1:print("Profile")
			
	case 13: print("SIM services")
		simServices=int(input('Enter an option: '))
		match simServices:
			case 1:print("SIM services")
 

	  
			
        
