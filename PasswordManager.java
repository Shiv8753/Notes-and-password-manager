import java.util.HashMap;

public class PasswordManager {
    private HashMap<String, String> passwords;

    public PasswordManager() {
        passwords = new HashMap<>();
    }

    public void addPassword(String site, String password) {
        passwords.put(site, password);
    }

    public String getPassword(String site) {
        return passwords.get(site);
    }

    public void removePassword(String site) {
        passwords.remove(site);
    }
}
