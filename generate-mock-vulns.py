from faker import Faker
from faker_security.providers import SecurityProvider

fake = Faker()
fake.add_provider(SecurityProvider)

# Generate a CVSSv3 vector
cvss_vector = fake.cvss3()
print(f"CVSSv3 Vector: {cvss_vector}")

# Generate a CVE identifier
cve_id = fake.cve()
print(f"CVE Identifier: {cve_id}")

# Generate an npm semantic version range
npm_range = fake.npm_semver_range()
print(f"NPM Semver Range: {npm_range}")