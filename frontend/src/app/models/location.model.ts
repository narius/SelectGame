import {User} from "./user.model";

export class Location{
  id: number;
  name: string;
  city: string;
  postalcode: string;
  is_public: boolean;
  street: string;
  owner: User;
}
