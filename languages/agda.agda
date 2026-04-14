module HelloWorld where
open import Agda.Builtin.IO using (IO)
open import Agda.Builtin.Unit renaming (⊤ to Unit)
open import Agda.Builtin.String using (String)
postulate putStrLn : String -> IO Unit
main : IO Unit
main = putStrLn "Hello world!"
