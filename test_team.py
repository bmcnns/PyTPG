def test_mutations_add_programs():
	"""
	Tests that mutations can add an existing program to a team.
	"""
	assert False

def test_mutations_never_exceed_maximum_programs_on_team():
	"""
	Tests that mutations will never add more programs than the maximum amount to a team.
	"""
	assert False

def test_mutations_remove_programs():
	"""
	Tests that mutations can remove a program from a team.
	"""
	assert False

def test_mutations_never_remove_all_programs():
	"""
	Tests that mutations will never remove the last program from a team.
	"""
	assert False

def test_mutations_create_new_programs():
	"""
	Tests that mutations can create a new program and assign it to the team.
	"""
	assert False

def test_mutations_swap_program_action():
	"""
	Tests that mutations can swap program's actions
	"""
	assert False

def test_mutations_create_program_team_references():
	"""
	Tests that mutations can cause a program to reference another team
	"""
	assert False

def test_mutations_does_not_remove_all_atomic_actions():
	"""
	Tests that mutations are guaranteed to leave at least one atomic action.
	"""
	assert False

def test_teams_do_not_evaluate_cycles():
	"""
	Tests that cycles will be avoided during action selection.
	"""
	assert False

def test_team_pointers_always_reach_atomic_action():
	"""
	Tests that following a team pointer will always eventually lead to an atomic action.
	"""
	assert False
