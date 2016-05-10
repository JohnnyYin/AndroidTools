on run args
	if (count args) is 0 then
		set command to "clear; cd ~"
	else
		set command to (first item of args)
	end if
	
	tell application "System Events"
		-- some versions might identify as "iTerm2" instead of "iTerm"
		set isRunning to (exists (processes where name is "iTerm")) or (exists (processes where name is "iTerm2"))
	end tell
	
	tell application "iTerm"
		activate
		set hasNoWindows to ((count of windows) is 0)
		if isRunning and hasNoWindows then
			create window with default profile
		end if
		select first window
		
		tell the first window
			if isRunning and hasNoWindows is false then
				create tab with default profile
			end if
			tell current session to write text command
		end tell
	end tell
end run