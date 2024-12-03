
function addSpaces(s: string, spaces: number[]): string {
    let new_string = ""
    let last_space = 0
    for(const space of spaces) {
        new_string += s.slice(last_space, space) + " "
        last_space = space
    }
    return new_string + s.slice(last_space)
};