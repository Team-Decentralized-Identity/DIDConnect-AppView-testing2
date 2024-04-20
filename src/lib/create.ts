import { AtpAgent, AtpAgentCreateAccountOpts, ComAtprotoServerCreateAccount } from "@atproto/api";

// Define the input parameters based on your API schema
interface AccountCreationParams {
  handle: string; // required
  email: string;
  password: string;
  // Include other optional parameters from your schema if needed
}

// Initialize your AtpAgent with the appropriate configuration
const SES_LOCAL_STORAGE_KEY = "sess";
const agentDID = new AtpAgent({
  service: "https://didconnect.tech",
  persistSession: (evt, sess) => {
    localStorage.setItem(SES_LOCAL_STORAGE_KEY, JSON.stringify(sess));
  },
});

// Function to create a new account using the AtpAgent
export const createAccount = async (params: AccountCreationParams): Promise<ComAtprotoServerCreateAccount.Response> => {
  try {
    // Prepare the options for the API call according to the required AtpAgentCreateAccountOpts interface
    const opts: AtpAgentCreateAccountOpts = {
      email: params.email,
      handle: params.handle,
      password: params.password,
      // Add other properties if required by the API
    };

    // Execute the API call
    const response: ComAtprotoServerCreateAccount.Response = await agentDID.createAccount(opts);

    // If the call returns without throwing, assume it was successful
    console.log('Account created successfully:', response);
    return response; // Use the correct response type from ComAtprotoServerCreateAccount

  } catch (error) {
    console.error('Error creating account:', error);
    throw error; // Rethrow or handle the error as appropriate for your application
  }
};
