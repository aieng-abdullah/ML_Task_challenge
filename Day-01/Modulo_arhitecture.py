# input 
seconds= 44444

hours= seconds // 3600



remaining_seconds= seconds % 3600

minutes= remaining_seconds // 60

seconds_final= remaining_seconds % 60

print(f"{hours}:{minutes}:{seconds_final}")