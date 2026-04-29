using System.Net.Http;
using System.Net.Http.Json;
using System.Text.Json;

string request = Console.ReadLine();

var content = new
{
    model = "gpt-oss:120b-cloud",
    messages = new[] {new {role = "user", content = request}},
    stream = false
};

var client = new HttpClient();

JsonContent contentJSON = JsonContent.Create(content);
var response = await client.PostAsync("http://localhost:11434/api/chat", contentJSON);

var result = await response.Content.ReadAsStringAsync();

var resultJSON = JsonSerializer.Deserialize<ChatResponse>(result);

Console.WriteLine(resultJSON.message.content);
public class ChatResponse
{
    public Message1 message {  get; set; }
}

public class Message1
{
    public string role { get; set; }
    public string content { get; set; }
}
