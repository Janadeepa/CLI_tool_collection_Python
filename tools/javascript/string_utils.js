function main(args) {
    str = args[0];
    if (args[1] == 'upper') {
        console.log(str.toUpperCase());
    } else if (args[1] == 'lower') {
        console.log(str.toLowerCase());
    } else {
        throw new Error("Invalid operation");
    }
}
