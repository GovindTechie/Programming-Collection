public class RemoveDoubleSequenceCharacters {

    public static void main(String[] args) {
        String input = "bbthhfccuukkllrr";
        System.out.println("Original String: " + input);

        StringBuilder result = new StringBuilder();
        int i = 0;
        while (i < input.length()) {
            result.append(input.charAt(i));
            int j = i + 1;
            while (j < input.length() && input.charAt(j) == input.charAt(i)) {
                j++;
            }
            i = j + 1; // Skip the next character to remove the double character sequence.
        }

        System.out.println("Removed double character String: " + result.toString());
    }
}
